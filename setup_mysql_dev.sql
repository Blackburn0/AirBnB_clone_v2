-- Sets up a simple database for development: hbnb_dev_db
-- Creates a new user: hbnb_dev
-- Grants 'hbnb_dev' All Privileges on the new development database: hbnb_dev_db
-- Grants 'hbnb_dev' SELECT privilege on the 'performance_schema' database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
