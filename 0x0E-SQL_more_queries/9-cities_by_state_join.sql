-- script that lists all cities contained in the database hbtn_0d_usa

SELECT cities.name, cities.id, states.name
FROM cities INNER JOIN states 
ON states.id = cities.state_id 
ORDER BY id;