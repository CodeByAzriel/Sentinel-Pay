CREATE DATABASE IF NOT EXISTS sentinel_pay;

USE sentinel_pay;

CREATE TABLE IF NOT EXISTS clean_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(10),
    amount DECIMAL(10,2),
    location VARCHAR(50),
    timestamp DATETIME,
    flag VARCHAR(20)
);