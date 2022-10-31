-- 1

SELECT name, language, percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC;

-- 2

SELECT countries.name, COUNT(*) FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name, country_id
ORDER BY COUNT(*) DESC;

-- 3

SELECT cities.name, cities.population FROM cities
WHERE country_id = 136 AND cities.population > 500000;

--  4

SELECT name, language, percentage FROM countries
JOIN languages on countries.id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;

-- 5

SELECT name, surface_area, population FROM countries
WHERE population > 100000 AND surface_area < 501;

-- 6

SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

-- 7

SELECT countries.name, cities.name, district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE district = "Buenos Aires" AND cities.population > 500000

-- 8

SELECT region, COUNT(*) as countries FROM countries
GROUP BY region
ORDER BY COUNT(*) DESC;