-- Create a database: hbnb_dev_db
-- Create a new user: hbnb_dev@localhost password: hbnb_dev_pwd
-- Grant all privilages to hbnb_dev@localhost on hbnb_dev_db
-- Grant select privilage to hbnb_dev@localhost on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
