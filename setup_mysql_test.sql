-- Create a database: hbnb_test_db
-- Create a new user: hbnb_test@localhost password: hbnb_test_pwd
-- Grant all privilages to hbnb_test@localhost on hbnb_dev_db
-- Grant select privilage to hbnb_test@localhost on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
