SELECT name from movies
JOIN stars on stars.movie_id = movies.id
JOIN people on people.id = stars.person_id
WHERE title = "Toy Story";