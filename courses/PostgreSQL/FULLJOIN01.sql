SELECT name AS country, code, region, basic_unit
FROM countries
FULL JOIN currencies
USING (code)
WHERE countries.region = 'North America' OR countries.region IS NULL
ORDER BY region;
