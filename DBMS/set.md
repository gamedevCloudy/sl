Certainly! Below are the SQL queries to solve the given problem statement:

```sql
-- Creating tables with appropriate constraints

CREATE TABLE Account (
    Acc_no INT PRIMARY KEY,
    branch_name VARCHAR(255),
    balance DECIMAL(10, 2),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE branch (
    branch_name VARCHAR(255) PRIMARY KEY,
    branch_city VARCHAR(255),
    assets DECIMAL(15, 2)
);

CREATE TABLE customer (
    cust_name VARCHAR(255) PRIMARY KEY,
    cust_street VARCHAR(255),
    cust_city VARCHAR(255)
);

CREATE TABLE Depositor (
    cust_name VARCHAR(255),
    acc_no INT,
    PRIMARY KEY (cust_name, acc_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (acc_no) REFERENCES Account(Acc_no)
);

CREATE TABLE Loan (
    loan_no INT PRIMARY KEY,
    branch_name VARCHAR(255),
    amount DECIMAL(15, 2),
    FOREIGN KEY (branch_name) REFERENCES branch(branch_name)
);

CREATE TABLE Borrower (
    cust_name VARCHAR(255),
    loan_no INT,
    PRIMARY KEY (cust_name, loan_no),
    FOREIGN KEY (cust_name) REFERENCES customer(cust_name),
    FOREIGN KEY (loan_no) REFERENCES Loan(loan_no)
);

-- Queries to solve the given problems

-- Q1. Find the names of all branches in the loan relation.
SELECT DISTINCT branch_name FROM Loan;

-- Q2. Find all loan numbers for loans made at Akurdi Branch with loan amount > 12000.
SELECT loan_no FROM Loan WHERE branch_name = 'Akurdi' AND amount > 12000;

-- Q3. Find all customers who have a loan from the bank. Find their names, loan_no, and loan amount.
SELECT c.cust_name, b.loan_no, l.amount
FROM customer c
JOIN Borrower b ON c.cust_name = b.cust_name
JOIN Loan l ON b.loan_no = l.loan_no;

-- Q4. List all customers in alphabetical order who have a loan from the Akurdi branch.
SELECT c.*
FROM customer c
JOIN Borrower b ON c.cust_name = b.cust_name
JOIN Loan l ON b.loan_no = l.loan_no
WHERE l.branch_name = 'Akurdi'
ORDER BY c.cust_name;

-- Q5. Find all customers who have an account or loan or both at the bank.
SELECT DISTINCT c.cust_name
FROM customer c
LEFT JOIN Depositor d ON c.cust_name = d.cust_name
LEFT JOIN Borrower b ON c.cust_name = b.cust_name
WHERE d.cust_name IS NOT NULL OR b.cust_name IS NOT NULL;

-- Q6. Find all customers who have both an account and a loan at the bank.
SELECT c.cust_name
FROM customer c
JOIN Depositor d ON c.cust_name = d.cust_name
JOIN Borrower b ON c.cust_name = b.cust_name;

-- Q7. Find all customers who have an account but no loan at the bank.
SELECT c.cust_name
FROM customer c
LEFT JOIN Borrower b ON c.cust_name = b.cust_name
WHERE b.cust_name IS NULL;

-- Q8. Find the average account balance at Akurdi branch.
SELECT AVG(balance) AS avg_balance
FROM Account
WHERE branch_name = 'Akurdi';

-- Q9. Find the average account balance at each branch.
SELECT branch_name, AVG(balance) AS avg_balance
FROM Account
GROUP BY branch_name;

-- Q10. Find the number of depositors at each branch.
SELECT branch_name, COUNT(DISTINCT cust_name) AS num_depositors
FROM Depositor
GROUP BY branch_name;

-- Q11. Find the branches where the average account balance > 12000.
SELECT branch_name
FROM Account
GROUP BY branch_name
HAVING AVG(balance) > 12000;

-- Q12. Find the number of tuples in the customer relation.
SELECT COUNT(*) AS num_tuples FROM customer;

-- Q13. Calculate the total loan amount given by the bank.
SELECT SUM(amount) AS total_loan_amount FROM Loan;

-- Q14. Delete all loans with a loan amount between 1300 and 1500.
DELETE FROM Loan
WHERE amount BETWEEN 1300 AND 1500;

-- Q15. Delete all tuples at every branch located in Nigdi.
DELETE FROM branch
WHERE branch_city = 'Nigdi';

-- Q16. Create a synonym for the customer table as cust.
CREATE SYNONYM cust FOR customer;

-- Q17. Create sequence roll_seq and use it in the student table for the roll_no column.
CREATE SEQUENCE roll_seq START WITH 1 INCREMENT BY 1;
CREATE TABLE student (
    roll_no INT DEFAULT roll_seq.NEXTVAL PRIMARY KEY,
    student_name VARCHAR(255)
);
```

These queries cover the requested operations and should help you solve the given problems. Make sure to adjust the queries based on your specific database requirements.