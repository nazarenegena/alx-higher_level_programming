--script that uses the hbtn_0d_tvshows db
--listing all genres linked to the show
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN shows_genres ON shows_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_shows.id = shows_genres.show_id AND tv_shows.title = 'Dexter'
WHERE tv_shows.id IS NULL
ORDER BY tv_genres.name ASC;
