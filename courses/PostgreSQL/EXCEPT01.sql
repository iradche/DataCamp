SELECT capital
FROM countries
EXCEPT
SELECT name 
FROM cities
ORDER BY capital ASC;
