-- Write a SQL script that creates a table users following these requirements:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null
-- If the table already exists, your script should not fail

SELECT origin, sum(fans) as nb_fans
FROM metal_bands
group by origin
ORDER BY nb_fans DESC
