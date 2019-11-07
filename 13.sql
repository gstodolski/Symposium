SELECT name FROM (SELECT movies.id FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Kevin Bacon" AND birth = "1958") AS bacon_movies
JOIN stars ON bacon_movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name != "Kevin Bacon"
GROUP BY name;