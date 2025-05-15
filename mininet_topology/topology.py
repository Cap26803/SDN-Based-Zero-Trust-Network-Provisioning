#!/usr/bin/env python3
import os
import time
import subprocess
import json
from datetime import datetime
import threading

from db_config import get_db_connection
from mininet.cli import CLI
from mininet.log import info, setLogLevel
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch


def check_ip(ip):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE ip=%s", (ip,))
    result = cursor.fetchone()
    db.close()
    return result


def log_attack(ip):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO attack_logs (unknown_ip, timestamp, action) VALUES (%s, NOW(), 'blocked')", (ip,))
    db.commit()
    db.close()


def block_ip(switch, ip):
    subprocess.run([
        'ovs-ofctl', 'add-flow', switch,
        f"priority=100,ip,nw_src={ip},actions=drop"
    ])
    print(f"[+] IP {ip} Blocked at {switch}")


def ensure_attack_log_exists():
    if not os.path.exists('static'):
        os.makedirs('static')

    if not os.path.exists('static/attacks.json'):
        with open('static/attacks.json', 'w') as f:
            json.dump({"attacks": []}, f, indent=4)


def update_admin_json(ip):
    ensure_attack_log_exists()

    with open('static/attacks.json', 'r') as f:
        data = json.load(f)

    data['attacks'].append({'ip': ip, 'time': str(datetime.now())})

    with open('static/attacks.json', 'w') as f:
        json.dump(data, f, indent=4)


def monitor_ping_from_attacker(attacker):
    """
    Monitors the Mininet CLI for ping commands issued from attacker
    and blocks the attacker when a ping command is executed.
    """
    while True:
        # Continuously monitor for ping commands from attacker
        # We will use Mininet's CLI to monitor 'ping' command
        user_input = input("Mininet> ")  # Capture user input in Mininet CLI
        if f"{attacker.name} ping" in user_input:
            print(f"[!] {attacker.name} sent a ping, blocking {attacker.name} immediately.")
            block_ip('s1', attacker.IP())
            log_attack(attacker.IP())
            update_admin_json(attacker.IP())
            break  # After blocking, stop monitoring


def myNetwork():
    net = Mininet(controller=Controller, switch=OVSKernelSwitch)

    c0 = net.addController('c0')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    hosts = {}

    # Adding 25 students
    for i in range(1, 26):
        hosts[f"h{i}"] = net.addHost(f"h{i}", ip=f"10.0.0.{i}")

    # Adding 8 faculty
    for i in range(26, 34):
        hosts[f"f{i-25}"] = net.addHost(f"f{i-25}", ip=f"10.0.0.{i}")

    # Adding 1 admin
    admin = net.addHost("admin", ip="10.0.0.90")

    # Adding 3 attackers
    attackers = []
    for i in range(1, 4):
        attacker = net.addHost(f"attacker{i}", ip=f"10.0.0.9{i}")
        attackers.append(attacker)

    # Link students to switch s1
    for i in range(1, 26):
        net.addLink(s1, hosts[f"h{i}"])

    # Link faculty to switch s2
    for i in range(26, 34):
        net.addLink(s2, hosts[f"f{i-25}"])

    # Link admin to switch s3
    net.addLink(s3, admin)

    # Link attackers to switch s3
    for attacker in attackers:
        net.addLink(s3, attacker)

    # Switch connections
    net.addLink(s1, s2)
    net.addLink(s2, s3)

    net.build()
    c0.start()
    s1.start([c0])
    s2.start([c0])
    s3.start([c0])

    # Start the ping monitoring in separate threads for attackers
    for attacker in attackers:
        monitor_thread = threading.Thread(target=monitor_ping_from_attacker, args=(attacker,))
        monitor_thread.daemon = True
        monitor_thread.start()

    # Use the CLI to interact with Mininet after setting up the network
    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()

