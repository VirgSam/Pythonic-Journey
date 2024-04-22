/*Practicing where statements
 Write a query that will print the name and price of all phones that sold greater than 500o units*/

SELECT name, price
FROM
phones
WHERE
units_sold > 5000;

/*Practicing where statements
 Write a query that will select the name and manufacturer for all phones created by apple or Samsung*/
SELECT name, manufacturer
FROM
phones
WHERE 
manufacturer ='Apple'
OR
manufacturer ='Samsung';