--script that creates MySQL server user at user_0d_1
--password should be set to the user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
