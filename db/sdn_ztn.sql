CREATE DATABASE IF NOT EXISTS sdn_ztn;
USE sdn_ztn;

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50),
password VARCHAR(50),
role VARCHAR(20),
ip VARCHAR(20)
);
-- Admin
INSERT INTO users (username, password, role, ip) VALUES 
('admin', 'admin123', 'admin', '10.0.0.90');

-- Faculties
INSERT INTO users (username, password, role, ip) VALUES
('faculty1', 'faculty1', 'faculty', '10.0.0.26'),
('faculty2', 'faculty2', 'faculty', '10.0.0.27'),
('faculty3', 'faculty3', 'faculty', '10.0.0.28'),
('faculty4', 'faculty4', 'faculty', '10.0.0.29'),
('faculty5', 'faculty5', 'faculty', '10.0.0.30'),
('faculty6', 'faculty6', 'faculty', '10.0.0.31'),
('faculty7', 'faculty7', 'faculty', '10.0.0.32'),
('faculty8', 'faculty8', 'faculty', '10.0.0.33');

-- Students (bcs01 to bcs25)
INSERT INTO users (username, password, role, ip) VALUES
('bcs01', 'student1', 'student', '10.0.0.1'),
('bcs02', 'student2', 'student', '10.0.0.2'),
('bcs03', 'student3', 'student', '10.0.0.3'),
('bcs04', 'student4', 'student', '10.0.0.4'),
('bcs05', 'student5', 'student', '10.0.0.5'),
('bcs06', 'student6', 'student', '10.0.0.6'),
('bcs07', 'student7', 'student', '10.0.0.7'),
('bcs08', 'student8', 'student', '10.0.0.8'),
('bcs09', 'student9', 'student', '10.0.0.9'),
('bcs10', 'student10', 'student', '10.0.0.10'),
('bcs11', 'student11', 'student', '10.0.0.11'),
('bcs12', 'student12', 'student', '10.0.0.12'),
('bcs13', 'student13', 'student', '10.0.0.13'),
('bcs14', 'student14', 'student', '10.0.0.14'),
('bcs15', 'student15', 'student', '10.0.0.15'),
('bcs16', 'student16', 'student', '10.0.0.16'),
('bcs17', 'student17', 'student', '10.0.0.17'),
('bcs18', 'student18', 'student', '10.0.0.18'),
('bcs19', 'student19', 'student', '10.0.0.19'),
('bcs20', 'student20', 'student', '10.0.0.20'),
('bcs21', 'student21', 'student', '10.0.0.21'),
('bcs22', 'student22', 'student', '10.0.0.22'),
('bcs23', 'student23', 'student', '10.0.0.23'),
('bcs24', 'student24', 'student', '10.0.0.24'),
('bcs25', 'student25', 'student', '10.0.0.25');

-- Attackers (Optional: For detection, not for login)
INSERT INTO users (username, password, role, ip) VALUES
('attacker1', 'attacker', 'unknown', '10.0.0.91'),
('attacker2', 'attacker', 'unknown', '10.0.0.92'),
('attacker3', 'attacker', 'unknown', '10.0.0.93');
