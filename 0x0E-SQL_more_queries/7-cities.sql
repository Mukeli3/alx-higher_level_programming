-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on the MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id FOREIGN KEY(stateid) REFERENCES states(stateid) NOT NULL, name VARCHAR(256) NOT NULL);
