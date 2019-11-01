SELECT name FROM movies
JOIN stars on movies.id = stars.movie_id
JOIN people on stars.person_id = people.id
WHERE year = "2004"
GROUP BY person_id
ORDER BY birth ASC;