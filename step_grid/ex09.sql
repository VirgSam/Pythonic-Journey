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