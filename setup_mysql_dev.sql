--   Prepare a MySQL serverfor the project
--   Database hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd.
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   Grants SELECT privilege for hbnb_dev on performance.

--   Create database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--   Create user hbnb_dev if he doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--   Grant all privileges on hbnb_dev_db and all its tables to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--   Grant SELECT privilege on performance_schema db and all its tables to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

--   Flush privileges - effect changes
FLUSH PRIVILEGES;
