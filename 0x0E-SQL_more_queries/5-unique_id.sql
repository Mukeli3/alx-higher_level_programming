-- creates the table unique_id on the MySQL server
-- Sets the id column default value to 1 (DEFAULT 1)
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
