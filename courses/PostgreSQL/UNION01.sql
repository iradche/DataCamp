SELECT country_code 
FROM cities
UNION 
SELECT code
FROM currencies
ORDER BY country_code;
