--   Prepare a test MySQL serverfor the project
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance.

--   Create database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--   Create user hbnb_test if he doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--   Grant all privileges on hbnb_test_db and all its tables to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

--   Grant SELECT privilege on performance_schema db and all its tables to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

--   Flush privileges - effect changes
FLUSH PRIVILEGES;
