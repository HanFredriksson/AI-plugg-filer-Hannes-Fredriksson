 -- Av alla audiosp�r, vilken artist har l�ngst total speltid?

 select * from music.artists;
 select * from music.tracks where MediaTypeId <> 3;
 select * from music.media_types;

select
	ar.Name,
	sum(tr.Milliseconds)/1000 as total_track_time_s,
	count(TrackId) as total_nbr_tracks,
	(sum(tr.Milliseconds)/count(TrackId))/1000 as avg_track_time_sec
from music.tracks tr
	left join music.albums al on tr.AlbumId = al.AlbumId
	left join music.artists ar on al.ArtistId = ar.ArtistId
where 
	MediaTypeId <> 3
group by 
	ar.Name
order by 
	total_track_time_s desc
 

 -- Vad �r den genomsnittliga speltiden p� den artistens l�tar?
DECLARE @Playtime TABLE (
	name nvarchar(max),
	playtime int
)
 
INSERT INTO @Playtime
	SELECT ar.Name, avg(tr.Milliseconds)/1000
	FROM music.tracks tr
		left join music.albums al on tr.AlbumId = al.AlbumId
		left join music.artists ar on al.ArtistId = ar.ArtistId
	WHERE MediaTypeId<>3 and ar.name = 'Iron maiden'
	GROUP BY ar.Name
 
SELECT  Avg (playtime) as 'Average playtime, s'
FROM @Playtime


-- Vad �r den sammanlagda filstorleken f�r all video?

select
    concat(round(convert(float, sum(convert(bigint, t.bytes))) / power(1024, 3), 1), ' GIB') as 'Total Size'
from
    music.tracks t
WHERE
    t.MediaTypeId = 3;


-- Vilket �r det h�gsta antal artister som finns p� en enskild spellista?

select -- top 1
	mpl.PlaylistId,
	mpl.Name,
	count(distinct(mal.ArtistId)) as 'Number of Artists on playlist'
	into #ArtistsPerPlaylist
from 
	music.playlists mpl
	left join music.playlist_track mpt on mpl.PlaylistId = mpt.PlaylistId
	left join music.tracks mt on mt.TrackId = mpt.TrackId
	left join music.albums mal on mal.AlbumId=mt.AlbumId
	left join music.artists mar on mar.ArtistId = mal.ArtistId
group by mpl.PlaylistId, mpl.Name

select * from #ArtistsPerPlaylist order by 'Number of Artists on playlist' desc



-- Vilket �r det genomsnittliga antalet artister per spellista?

select avg([Number of Artists on playlist]) from #ArtistsPerPlaylist

