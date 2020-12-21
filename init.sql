CREATE DATABASE IF NOT EXISTS Tags;
CREATE USER 'dbadmin'@'%' IDENTIFIED WITH mysql_native_password BY '1234';
GRANT ALL PRIVILEGES ON Tags.* TO 'dbadmin'@'%';
