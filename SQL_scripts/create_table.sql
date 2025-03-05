-- Create Database
CREATE DATABASE IF NOT EXISTS loan_analysis;


-- Use Database
USE loan_analysis;

-- Create Table
CREATE TABLE IF NOT EXISTS loan_data (
    LoanID VARCHAR(20) PRIMARY KEY,
    Age INT,
    Income FLOAT,
    LoanAmount FLOAT,
    CreditScore INT,
    MonthsEmployed INT,
    NumCreditLines INT,
    InterestRate FLOAT,
    DebtToIncomeRatio FLOAT,
    Education VARCHAR(50),
    EmploymentStatus VARCHAR(50),
    MaritalStatus VARCHAR(50),
    HomeOwnership VARCHAR(50),
    HasBankruptcies BOOLEAN,
    Purpose VARCHAR(100),
    PreviousDefaults BOOLEAN,
    OtherLoans BOOLEAN,
    LoanStatus VARCHAR(10)
);

-- Verify Table Structure
DESC loan_data;

USE loan_analysis;

ALTER TABLE loan_data MODIFY COLUMN LoanID VARCHAR(20);

SHOW TABLES;

DESC loan_data;

SELECT * FROM loan_data LIMIT 5;

SELECT COUNT(*) FROM loan_data;