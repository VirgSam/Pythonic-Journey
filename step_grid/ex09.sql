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