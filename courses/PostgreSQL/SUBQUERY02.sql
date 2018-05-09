-- select the appropriate fields
SELECT name, country_code, urbanarea_pop
-- from the cities table
FROM cities
-- with city name in the field of capital cities
WHERE name IN
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;
