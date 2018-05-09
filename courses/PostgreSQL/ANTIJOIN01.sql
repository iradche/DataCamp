SELECT code, name
FROM countries 
WHERE continent = 'Oceania'
AND code NOT IN
    (SELECT code 
     FROM currencies);
