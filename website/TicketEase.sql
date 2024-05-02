-- Create database
CREATE DATABASE IF NOT EXISTS TicketEase;

-- Grant privileges to 'root' user
GRANT ALL PRIVILEGES ON TicketEase.* TO 'root'@'localhost';

-- Use the database
USE TicketEase;

-- Create events table
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    venue VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INT NOT NULL
);

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create tickets table
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    ticket_type VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    quantity_available INT NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL
);

-- Create orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    ticket_id INT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id),
    quantity INT NOT NULL,
    total_amount FLOAT NOT NULL,
    order_date DATETIME NOT NULL
);

-- Create payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    payment_date DATETIME NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    status VARCHAR(50) NOT NULL
);
