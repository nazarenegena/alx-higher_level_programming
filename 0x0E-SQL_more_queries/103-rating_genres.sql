--script that lists all genres in the database by rating
--record displays tv_genresName/ratingsum
--sorting is in a descending order
SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN shows_genres ON shows_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = shows_genres.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
