from flask import Flask, jsonify, redirect, request, send_from_directory
from mininet_topology.db_config import get_db_connection
import json
import datetime
import os

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return redirect('/login.html')


# API for Login Authentication (with threshold alerts)
@app.route('/api/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT role FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    db.close()

    login_log_path = os.path.join('dashboard', 'admin', 'login_logs.json')
    fail_log_path = os.path.join('dashboard', 'admin', 'failed_logins.json')
    alert_path = os.path.join('dashboard', 'admin', 'password_reset.json')

    failed_data = {}
    if os.path.exists(fail_log_path):
        with open(fail_log_path, 'r') as f:
            failed_data = json.load(f)

    if result:
        role = result[0]

        log_entry = {
            'username': username,
            'role': role,
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if os.path.exists(login_log_path):
            with open(login_log_path, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data.append(log_entry)
        with open(login_log_path, 'w') as f:
            json.dump(data, f, indent=4)

        failed_data.pop(username, None)
        with open(fail_log_path, 'w') as f:
            json.dump(failed_data, f, indent=4)

        return jsonify({'status': 'success', 'role': role, 'username': username})
    else:
        failed_data[username] = failed_data.get(username, 0) + 1

        if failed_data[username] >= 5:
            reset_alert = {
                "username": username,
                "alert": "⚠️ Multiple failed login attempts detected. Please reset your password.",
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            if os.path.exists(alert_path):
                with open(alert_path, 'r') as f:
                    alerts = json.load(f)
            else:
                alerts = []

            if not any(entry["username"] == username for entry in alerts):
                alerts.append(reset_alert)
                with open(alert_path, 'w') as f:
                    json.dump(alerts, f, indent=4)

        with open(fail_log_path, 'w') as f:
            json.dump(failed_data, f, indent=4)

        return jsonify({'status': 'fail'})


# Add Marks
@app.route('/api/add_marks', methods=['POST'])
def add_marks():
    username = request.form['username']
    subject = request.form['subject']
    marks = request.form['marks']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO marks(username, subject, marks) VALUES (%s, %s, %s)", (username, subject, marks))
    db.commit()
    db.close()

    return jsonify({'message': 'Marks Added Successfully'})


# View All Marks (Faculty)
@app.route('/api/view_marks')
def view_marks():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT username, subject, marks FROM marks")
    data = cursor.fetchall()
    db.close()

    result = [{'username': row[0], 'subject': row[1], 'marks': row[2]} for row in data]
    return jsonify(result)


# View My Marks (Student)
@app.route('/api/my_marks')
def my_marks():
    username = request.args.get('username')
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT subject, marks FROM marks WHERE username=%s", (username,))
    data = cursor.fetchall()
    db.close()

    result = [{'subject': row[0], 'marks': row[1]} for row in data]
    return jsonify(result)


# Attack Logs for Admin
@app.route('/api/attack_logs')
def attack_logs():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, unknown_ip, timestamp, action FROM attack_logs ORDER BY id DESC")
    logs = cursor.fetchall()
    db.close()
    return jsonify(logs)


# Heatmap Data API
@app.route('/api/login_heatmap')
def login_heatmap():
    json_path = os.path.join('dashboard', 'admin', 'login_logs.json')
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            logs = json.load(f)
    else:
        logs = []

    heatmap_data = {}
    for entry in logs:
        date_str = entry['time'].split(' ')[0]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        timestamp = int(date_obj.timestamp())
        heatmap_data[timestamp] = heatmap_data.get(timestamp, 0) + 1

    return jsonify(heatmap_data)


# Password Reset Alerts API
@app.route('/api/password_reset_alerts')
def password_reset_alerts():
    alert_path = os.path.join('dashboard', 'admin', 'password_reset.json')
    if os.path.exists(alert_path):
        with open(alert_path, 'r') as f:
            alerts = json.load(f)
    else:
        alerts = []
    return jsonify(alerts)
    
    
# Reset Password API (after multiple failed attempts)
@app.route('/api/reset_password', methods=['POST'])
def reset_password():
    username = request.form.get('username')
    new_password = request.form.get('new_password')

    if not username or not new_password:
        return jsonify({"success": False, "message": "Username or new password missing."})

    # Update password in DB
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
    db.commit()
    db.close()

    # Remove from reset alert JSON if present
    alert_path = os.path.join('dashboard', 'admin', 'password_reset.json')
    if os.path.exists(alert_path):
        with open(alert_path, 'r') as f:
            alerts = json.load(f)

        # Remove this user from alerts
        alerts = [entry for entry in alerts if entry["username"] != username]

        with open(alert_path, 'w') as f:
            json.dump(alerts, f, indent=4)

    return jsonify({"success": True, "message": "✅ Password updated successfully."})



# ------------------ STATIC ROUTES ------------------

@app.route('/login.html')
def login_page():
    return send_from_directory('dashboard', 'login.html')

@app.route('/common/style.css')
def common_css():
    return send_from_directory('dashboard/common', 'style.css')

@app.route('/admin/<path:path>')
def admin_static(path):
    return send_from_directory('dashboard/admin', path)

@app.route('/faculty/<path:path>')
def faculty_static(path):
    return send_from_directory('dashboard/faculty', path)

@app.route('/student/<path:path>')
def student_static(path):
    return send_from_directory('dashboard/student', path)

@app.route('/libs/<path:path>')
def libs_static(path):
    return send_from_directory('dashboard/libs', path)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

