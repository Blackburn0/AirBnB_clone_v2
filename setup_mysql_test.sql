-- Sets up a simple database for development: hbnb_test_db
-- Creates a new user: hbnb_test
-- Grants 'hbnb_test' All Privileges on the new development database: hbnb_test_db
-- Grants 'hbnb_test' SELECT privilege on the 'performance_schema' database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
