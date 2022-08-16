-- script that lists all cities contained in the database hbtn_0d_usa
USE hbtn_0d_usa;
select cities.name, cities.id, and states.name
FROM cities INNER JOIN states 
ON states.id = cities.state_id 
ORDER BY id;