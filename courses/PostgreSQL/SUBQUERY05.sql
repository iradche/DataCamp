SELECT 	name, continent, inflation_rate
FROM countries
INNER JOIN economies
ON countries.code = economies.code
WHERE economies.year = 2015
    AND inflation_rate IN (
     SELECT max(inflation_rate) AS max_inf
     FROM 
        (SELECT countries.name, countries.continent, economies.inflation_rate
         FROM countries
         INNER JOIN economies
         ON countries.code = economies.code
         WHERE economies.year = 2015) AS subquery
     GROUP BY continent);


