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