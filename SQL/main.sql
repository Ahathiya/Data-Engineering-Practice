QUESTION

A payment system considers two transactions as potential duplicates if:

- Same CustomerID
- Same Amount
- Transaction time difference is less than or equal to 5 minutes

Return all duplicate transaction pairs.

SQL SCRIPT

CREATE TABLE Transactions (
    TransactionID INT,
    CustomerID INT,
    Amount DECIMAL(10,2),
    TransactionTime DATETIME
);

INSERT INTO Transactions VALUES
(1,101,250.00,'2026-06-01 10:00:00'),
(2,101,250.00,'2026-06-01 10:03:00'),
(3,101,250.00,'2026-06-01 10:15:00'),
(4,102,500.00,'2026-06-01 11:00:00'),
(5,102,500.00,'2026-06-01 11:04:00'),
(6,103,120.00,'2026-06-01 09:00:00'),
(7,103,150.00,'2026-06-01 09:03:00'),
(8,104,300.00,'2026-06-01 12:00:00'),
(9,104,300.00,'2026-06-01 12:05:00'),
(10,104,300.00,'2026-06-01 12:20:00');



EXPECTED OUTPUT

TransactionID1 | TransactionID2 | CustomerID | Amount | TimeDifferenceMinutes
----------------------------------------------------------------------------
1              | 2              | 101        | 250.00 | 3
4              | 5              | 102        | 500.00 | 4
8              | 9              | 104        | 300.00 | 5

 
-- A product price history table stores every price revision.
-- Find each continuous period during which the product price remained unchanged.
 
-- SQL SCRIPT
 
CREATE TABLE ProductPrices (
    ProductID INT,
    PriceDate DATE,
    Price DECIMAL(10,2)
);
 
INSERT INTO ProductPrices VALUES
(101,'2026-01-01',100),
(101,'2026-01-02',100),
(101,'2026-01-03',100),
(101,'2026-01-04',120),
(101,'2026-01-05',120),
(101,'2026-01-06',130),
 
(102,'2026-01-01',50),
(102,'2026-01-02',50),
(102,'2026-01-03',50),
(102,'2026-01-04',50),
 
(103,'2026-01-01',200),
(103,'2026-01-02',180),
(103,'2026-01-03',180),
(103,'2026-01-04',180),
(103,'2026-01-05',220);
 
select * from ProductPrices
 
-- EXPECTED OUTPUT
 
-- ProductID | Price | EffectiveStartDate | EffectiveEndDate | NumberOfDays
-- ------------------------------------------------------------------------
-- 101       | 100   | 2026-01-01         | 2026-01-03       | 3
-- 101       | 120   | 2026-01-04         | 2026-01-05       | 2
-- 101       | 130   | 2026-01-06         | 2026-01-06       | 1
-- 102       | 50    | 2026-01-01         | 2026-01-04       | 4
-- 103       | 200   | 2026-01-01         | 2026-01-01       | 1
-- 103       | 180   | 2026-01-02         | 2026-01-04       | 3
-- 103       | 220   | 2026-01-05         | 2026-01-05       | 1