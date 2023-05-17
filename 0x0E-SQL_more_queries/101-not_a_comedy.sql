--script that lists all the shows without the genre Comedy
--its in the databasehbtn_0d_tvshows
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN shows_genres ON shows_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_shows.id = shows_genres.show_id AND tv_shows.title = 'Dexter'
WHERE tv_shows.id IS NULL
ORDER BY tv_genres.name ASC;
