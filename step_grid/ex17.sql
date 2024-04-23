/*Using the Update Statement*/
UPDATE 
cities
SET
population = 39505000
WHERE
name = 'Tokyo';

/*Using the DELETE Statement*/
DELETE
FROM
cities
WHERE
name = 'Tokyo';

INSERT INTO cities(name,country,population,area)
VALUES
('Tokyo','Japan',39505000,8223);