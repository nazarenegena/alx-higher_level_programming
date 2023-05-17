--a script that uses the hbtn_0d_tvshows
-- the database to lists all genres of the show Dexter
SELECT genres.genre AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.genre
ORDER BY number_of_shows DESC;
