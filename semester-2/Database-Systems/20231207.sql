-- DBMS Practical 1 [complete]
-- Date: Thursday December 07th 2023

-- To display all databases
SHOW DATABASES;

-- To create a database
-- Syntax: CREATE DATABASE <database-name>
CREATE DATABASE nt01;

-- Switch to the 'nt01' database
USE nt01;

-- Show tables in the current database
SHOW TABLES;

-- Create a table 'persons' with columns: personid, lastname, firstname, address, contact
CREATE TABLE persons (personid INT, lastname VARCHAR(30), firstname VARCHAR(30), address VARCHAR(50), contact INT);

-- Create a table 'customer' with columns: customer_id, customer_name, contact_no, address, city
-- Set 'customer_id' as primary key and 'customer_name' as not null
CREATE TABLE customer (customer_id INT PRIMARY KEY, customer_name VARCHAR(15) NOT NULL, contact_no INT UNIQUE, address VARCHAR(25), city VARCHAR(15));

-- Create a table 'employee' with columns: emp_id, ename, sal
-- Set 'emp_id' as primary key
CREATE TABLE employee (emp_id INT PRIMARY KEY, ename VARCHAR(25), sal INT);

-- Insert values into the 'employee' table
INSERT INTO employee VALUES (1001, 'jack', 12000), (1002, 'mark', 13000);

-- Select columns 'ename' and 'sal' from the 'employee' table
SELECT ename, sal FROM employee;

-- Insert another record into the 'employee' table
INSERT INTO employee VALUES (1003, 'kate', 15000);

-- Select all columns from the 'employee' table
SELECT * FROM employee;

-- Update the 'employee' table, increase 'sal' by 5000 where 'sal' is 13000
UPDATE employee SET sal = sal + 5000 WHERE sal = 13000;

-- Delete a record from the 'employee' table where 'emp_id' is 1003
DELETE FROM employee WHERE emp_id = 1003;
