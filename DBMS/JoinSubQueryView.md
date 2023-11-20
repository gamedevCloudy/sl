Certainly! Here are the SQL queries to solve the given problem statement:

### 1. 
```sql
-- Creating tables
CREATE TABLE cust_mstr (
    cust_no INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255)
);

CREATE TABLE add_dets (
    code_no INT PRIMARY KEY,
    add1 VARCHAR(255),
    add2 VARCHAR(255),
    state VARCHAR(255),
    city VARCHAR(255),
    pincode VARCHAR(10)
);

-- Retrieving the address of the customer with Fname as 'xyz' and Lname as 'pqr'
SELECT a.add1, a.add2, a.state, a.city, a.pincode
FROM cust_mstr c
JOIN add_dets a ON c.cust_no = a.code_no
WHERE c.fname = 'xyz' AND c.lname = 'pqr';
```

### 2. 
```sql
-- Creating tables
CREATE TABLE cust_mstr (
    custno INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255)
);

CREATE TABLE acc_fd_cust_dets (
    codeno INT PRIMARY KEY,
    acc_fd_no INT
);

CREATE TABLE fd_dets (
    fd_sr_no INT PRIMARY KEY,
    amt DECIMAL(10, 2)
);

-- Listing customers holding fixed deposits of amount more than 5000
SELECT c.*
FROM cust_mstr c
JOIN acc_fd_cust_dets acd ON c.custno = acd.codeno
JOIN fd_dets fd ON acd.acc_fd_no = fd.fd_sr_no
WHERE fd.amt > 5000;
```

### 3.
```sql
-- Creating tables
CREATE TABLE emp_mstr (
    empno INT PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    m_name VARCHAR(255),
    dept VARCHAR(255),
    desg VARCHAR(255),
    branch_no INT
);

CREATE TABLE branch_mstr (
    name VARCHAR(255),
    b_no INT PRIMARY KEY
);

-- Listing employee details along with branch names to which they belong
SELECT e.*, b.name AS branch_name
FROM emp_mstr e
JOIN branch_mstr b ON e.branch_no = b.b_no;
```

### 4.
```sql
-- Creating tables
CREATE TABLE emp_mstr (
    emp_no INT PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    m_name VARCHAR(255),
    dept VARCHAR(255)
);

CREATE TABLE cntc_dets (
    code_no INT PRIMARY KEY,
    cntc_type VARCHAR(255),
    cntc_data VARCHAR(255)
);

-- Listing employee details along with contact details using left outer join and right join
-- Left outer join
SELECT e.*, c.cntc_type, c.cntc_data
FROM emp_mstr e
LEFT JOIN cntc_dets c ON e.emp_no = c.code_no;

-- Right join
SELECT e.*, c.cntc_type, c.cntc_data
FROM emp_mstr e
RIGHT JOIN cntc_dets c ON e.emp_no = c.code_no;
```

### 5.
```sql
-- Creating tables
CREATE TABLE cust_mstr (
    cust_no INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255)
);

CREATE TABLE add_dets (
    code_no INT PRIMARY KEY,
    pincode VARCHAR(10)
);

-- Listing customers who do not have bank branches in their vicinity
SELECT c.*
FROM cust_mstr c
LEFT JOIN add_dets a ON c.cust_no = a.code_no
WHERE a.code_no IS NULL OR a.pincode IS NULL;
```

### 6.
```sql
-- a) Creating a view on the borrower table
CREATE VIEW borrower_view AS
SELECT cust_name, loan_no
FROM Borrower;

-- Insert, Update, Delete operations on the view
-- INSERT INTO borrower_view (cust_name, loan_no) VALUES ('John', 101);
-- UPDATE borrower_view SET loan_no = 102 WHERE cust_name = 'John';
-- DELETE FROM borrower_view WHERE cust_name = 'John';

-- b) Creating a view on borrower and depositor table
CREATE VIEW borrower_depositor_view AS
SELECT b.cust_name
FROM Borrower b
UNION
SELECT d.cust_name
FROM Depositor d;

-- Insert, Update, Delete operations on the view
-- INSERT INTO borrower_depositor_view (cust_name) VALUES ('John');
-- UPDATE borrower_depositor_view SET cust_name = 'Jack' WHERE cust_name = 'John';
-- DELETE FROM borrower_depositor_view WHERE cust_name = 'Jack';

-- c) Creating an updateable view on the borrower table
CREATE VIEW updatable_borrower_view AS
SELECT cust_name, loan_no
FROM Borrower
WITH CHECK OPTION;

-- Insert, Update, Delete operations on the view
-- INSERT INTO updatable_borrower_view (cust_name, loan_no) VALUES ('John', 101);
-- UPDATE updatable_borrower_view SET loan_no = 102 WHERE cust_name = 'John';
-- DELETE FROM updatable_borrower_view WHERE cust_name = 'John';
```

These queries cover the requested operations using various concepts like joins, sub-queries, and views. Make sure to adjust the queries based on your specific database requirements.