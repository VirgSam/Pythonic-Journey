-- String operators and functions
-- Concatenation using pipe
SELECT name || ',' || country FROM cities;

SELECT name || ',' || country AS location FROM cities;

-- Concatenation using concat function
SELECT CONCAT(name, ', ', country) AS location FROM cities;