-- imoprt database from hbtn_0d_tvshows
-- shows linked to each
SELECT X.`name` AS `genre`,
COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS x
INNER JOIN `tv_show_genres` AS y
ON x.`id` = y.`genre_id`
GROUP BY x.`name`
ORDER BY `number_of_shows` DESC;
