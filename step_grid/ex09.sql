/*Using Calculated columns
Take a look at the following table called phones. this table had already been inserted into the database
write a query that will select the name of each phone and calculate the total revenue for each phone(price x units_sold)
Rename this calculated column as revenue */
CREATE TABLE phones (
    name VARCHAR(50),
    manufacturer VARCHAR(20),
    price INTEGER,
    units_sold INTEGER
);

INSERT INTO phones(name,manufacturer,price,units_sold)
VALUES
('N1280','Nokia',199,1925),
('Iphone 4','Apple',399,9436),
('Galaxy S','Samsung',299,2359),
('S5620 Monte','Samsung',250,2385),
('N8','Nokia',150,7543);

SELECT name,manufacturer, price * units_sold AS revenue
FROM phones;

INSERT INTO phones(name,manufacturer,price,units_sold)
VALUES
('Droid','Motorola',150,8395),
('Wave S8500','Samsung',175,9259);

-- Write query here to update the 'units_sold' of the phone with name 'N8' to 8543
UPDATE phones
SET units_sold  = 8543
WHERE name='N8';


-- Write query here to select all rows and columns of the 'phones' table
select * from phones;

-- Write your delete SQL here
delete 
from phones
where manufacturer = 'Samsung';

-- Write query here to select all rows and columns from phones
select * from phones;

-- Practise exercise on Having
/*
Given a table of phones, print the names of manufacturers and total revenue (price * units_sold) for all phones.  
Only print the manufacturers who have revenue greater than 2,000,000 for all the phones they sold.
*/
-- update N8 value
UPDATE phones
SET units_sold = 7543
WHERE name = 'N8';

-- Insert samsung phones into table
INSERT INTO phones(name,manufacturer,price,units_sold)
VALUES
('Galaxy S','Samsung',299,2359),
('S5620 Monte','Samsung',250,2385),
('Wave S8500','Samsung',175,9259);

-- Query request
SELECT manufacturer, SUM(price*units_sold)
FROM phones
GROUP BY manufacturer
HAVING SUM(price*units_sold)> 2000000;

-- Practise exercise on Sorting, Offsetting and Limiting
/*Write a query that shows the names of only the second and third most expensive phones.*/
SELECT name
FROM phones
ORDER BY price DESC
LIMIT 2
OFFSET 1;

/* Practise exercise
Write a query that will print the manufacturer of phones where the phone's price is less than 170.  
Also print all manufacturer that have created more than two phones.*/
(
    SELECT manufacturer
    FROM phones
    WHERE price < 170
)
UNION
(
    SELECT manufacturer
    FROM phones
    GROUP BY manufacturer
    HAVING count(*)>2
);

/* Practise exercise 
Write a query that prints the name and price for each phone.  
In addition, print out the ratio of the phones price against max price of all phones (so price / max price).  
Rename this third column to price_ratio
*/
-- write first the query
SELECT MAX(price)
FROM phones;

-- insert above query into subquery
SELECT name, price, price/(
    SELECT MAX(price)
FROM phones
) AS price_ratio
FROM phones;

/* Practise exercise subquery
Calculate the average price of phones for each manufacturer.  
Then print the highest average price. 
Rename this value to max_average_price*/
SELECT MAX(p.average_price) AS max_average_price
FROM (SELECT AVG(price) AS average_price
FROM phones
GROUP BY manufacturer) AS p;

/*Subquery Where's
Write a query that prints out the name and price of phones that have a price greater 
than the Samsung S5620 Monte.
*/
-- first part
SELECT price
FROM phones
WHERE name = 'S5620 Monte';

-- second part
SELECT name,price
FROM phones 
WHERE price >(
    SELECT price
    FROM phones
    WHERE name = 'S5620 Monte'
);

/*
 Practice Your Subqueries!
Write a query that prints the name of all phones that have a price greater than all phones made by Samsung.
*/
-- First part
SELECT price
FROM phones
WHERE manufacturer = 'Samsung';

-- Second part
SELECT name
FROM phones
WHERE price>ALL (
    SELECT price
    FROM phones
    WHERE manufacturer = 'Samsung';
);

/*Practise query
Using subqueries print out the max price, min price and average price of all phones*/
SELECT (
    SELECT MAX(price)
    FROM phones) AS max_price,
       (
        SELECT MIN(price)
        FROM phones)AS min_price,
       (SELECT AVG(price) 
       FROM phones)AS avg_price;