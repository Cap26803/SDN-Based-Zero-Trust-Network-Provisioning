CREATE DATABASE IF NOT EXISTS sdn_ztn;
USE sdn_ztn;

CREATE TABLE users (
 id INT AUTO_INCREMENT PRIMARY KEY,
 username VARCHAR(50),
 password VARCHAR(50),
 role VARCHAR(20),
 ip VARCHAR(20)
);

CREATE TABLE attack_logs (
 id INT AUTO_INCREMENT PRIMARY KEY,
 unknown_ip VARCHAR(20),
 timestamp DATETIME,
 action VARCHAR(50)
);

INSERT INTO users(username,password,role,ip) VALUES
('admin','admin123','admin',NULL),
('h1','student1','student','10.0.0.1'),
('h2','student2','student','10.0.0.2'),
('h3','student3','student','10.0.0.3'),
('h4','student4','student','10.0.0.4'),
('h5','faculty1','faculty','10.0.0.5'),
('h6','faculty2','faculty','10.0.0.6');
