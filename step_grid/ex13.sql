-- Using the Where statement
SELECT name, area FROM cities WHERE area > 4000;

-- Using where statement with = operator
SELECT 
name, area 
FROM 
cities 
WHERE area = 8223;

-- Using where statement with != operator
SELECT 
name, area 
FROM 
cities 
WHERE area != 8223;

-- Using where statement with BETWEEN operator
SELECT 
name, area 
FROM 
cities 
WHERE area BETWEEN 2000 AND 4000;

-- Using where statement with IN operator
SELECT 
name, area 
FROM 
cities 
WHERE 
name 
IN ('Delhi','Shanghai');

SELECT 
name, area 
FROM 
cities 
WHERE 
area 
IN (3043,8223);

SELECT 
name, area 
FROM 
cities 
WHERE 
area 
NOT IN (3043,8223);

-- Using complex where statement with IN operator
SELECT 
name, area 
FROM 
cities 
WHERE 
area 
NOT IN (3043,8223) AND name = 'Delhi';

-- Using complex where statement with IN/OR operator
SELECT 
name, area 
FROM 
cities 
WHERE 
area 
NOT IN (3043,8223) 
OR name = 'Delhi'
OR name = 'Tokyo';