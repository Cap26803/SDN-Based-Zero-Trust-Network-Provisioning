# SDN-Based Zero Trust Network Provisioning

A Capstone Project implementing a Zero Trust Network (ZTN) security model using Software-Defined Networking (SDN) to enhance network security through access control and monitoring.

---

## 🔐 What is Zero Trust Network (ZTN)?

**Zero Trust Network (ZTN)** is a security architecture that follows the principle of “never trust, always verify.” It eliminates implicit trust by continuously validating users, devices, and services before granting access to network resources—regardless of whether the connection originates internally or externally.

### 🏫 ZTN in a University Scenario

In this project, ZTN is implemented in an academic setting as follows:

- **Role-Based Dashboards** ensure students, faculty, and admin users can access only authorized data and services.
- **Authentication & IP Validation** mechanisms enforce strict verification before granting access.
- **SDN Controller** monitors network traffic and dynamically blocks attackers based on their behavior.
- **Password Reset Alerts** notify users of suspicious activity, such as repeated failed logins.

This aligns with real-world university networks where internal and external threats must be contained, and access should be minimal and role-specific.

### 🌐 Applicability to Other Scenarios

The ZTN model used here is modular and adaptable. It can be extended to:

- **Corporate Networks** for employee access control
- **Healthcare Systems** to protect patient data
- **IoT Environments** for device validation
- **Government or Military** setups for sensitive operations

By modifying the user roles, network topology, and access policies, this architecture can be deployed in virtually any scenario demanding strong security and trust management.

---

## Project Overview

This project demonstrates the integration of Zero Trust principles with Software-Defined Networking (SDN) to create a secure and scalable network environment. The system ensures that no device or user is trusted by default, verifying every network interaction based on identity.

Using **Mininet** for network simulation and **Open vSwitch (OVS)** for traffic control, the system automatically detects unknown devices, blocks their communication using OpenFlow rules, and logs the events in both a **MySQL database** and **JSON files**. A role-based dashboard provides **Admin**, **Faculty**, and **Students** with controlled access and network visibility.

---

## Key Features

- **Role-Based Access Control**: Separate dashboards for Admin, Faculty, and Students with role-specific functionalities.
- **Real-Time Attack Detection**: Automatic blocking of unknown or unauthorized IP addresses using SDN flow rules.
- **Centralized Logging**: User activities and attacker attempts are logged in a MySQL database and JSON files.
- **Network Visualization**: Real-time network topology visualization using **Vis.js**.
- **Password Reset Alerts**: Alerts are triggered after suspicious login patterns.
- **Multi-Role Dashboard**: Interactive dashboards with login analytics, marks management, and threat alerts.

---

## Installation and Setup

### Prerequisites

- **Operating System**: Ubuntu 22.04 LTS  
- **Virtualization**: VirtualBox or Dual Boot  
- **Software Tools**:
  - Mininet
  - Open vSwitch (OVS)
  - MySQL Server 8.0
  - Flask
  - Python 3.10
  - MySQL Workbench

### Installation Steps

1. **Install Dependencies**:
    ```bash
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install python3 python3-pip mininet openvswitch-switch mysql-server mysql-workbench
    pip3 install flask mysql-connector-python
    ```

2. **Configure MySQL Database**:
    - Create a new database for the project.
    - Import the provided SQL schema file.
---

## Implementation

1. **Launch Network Simulation** (/mininet_topology):
    ```bash
    python3 topology.py
    ```

2. **Run the Web Application**:
    ```bash
    python3 run_server.py
    ```
---

## Usage

### Access the Web Interface

- Open a browser and navigate to: `http://localhost:5000`  
- Log in using the appropriate credentials:

  - **Admin**: `admin / admin123`  
  - **Faculty**: `f1 / faculty1`  
  - **Student**: `h1 / student1`

### Dashboard Functionalities

#### Admin Dashboard
- View real-time network topology  
- Monitor attack logs and blocked IPs  

#### Faculty Dashboard
- Add and manage student marks  
- View academic performance analytics

#### Student Dashboard
- View personal marks and progress  
- Receive password reset alerts for suspicious activity

---

## Testing

### Test Cases

| Test Case ID | Test Type              | Description                                   | Expected Result                   | Actual Result |
|--------------|------------------------|-----------------------------------------------|------------------------------------|---------------|
| TC1          | Role-Based Authentication | User is redirected to their respective dashboard | Pass                               | Pass          |
| TC2          | Unknown IP Detection   | Attacker IP is blocked and logged             | Pass                               | Pass          |
| TC3          | Login Attempt Threshold | Alert triggered after repeated failed logins | Pass                               | Pass          |
| TC4          | Dashboard Sync         | Live logs and attack alerts are displayed     | Pass                               | Pass          |
| TC5          | Faculty Dashboard      | Marks are stored and visible to students      | Pass                               | Pass          |
| TC6          | Student Dashboard      | Personalized data is displayed correctly      | Pass                               | Pass          |

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Acknowledgments

- **Contributors**: Chinmay Paranjape, Kushal Kaparatti, Chandsab Engineer, Prathamesh Chitnis  
- **Guidance**: Prof. U. V. Somanatti
- **Institution**: KLE Technological University’s Dr. M. S. Sheshgiri College of Engineering and Technology, Belagavi

---

## Note

This project is a **proof-of-concept** implementation. For production use, additional **security hardening** and **scalability improvements** are recommended.

Please report any issues or suggestions to the project maintainers.