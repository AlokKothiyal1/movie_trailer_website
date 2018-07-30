import fresh_tomatoes
import media

#instances of class Movie------------------------------------------------------
spider_man = media.Movie('SpiderMan HomeComing',
'Peter Parker is exploring the concept of becoming an Avenger.',
'http://www.joblo.com/posters/images/full/Spider-Man-Homecoming-poster-2-large.jpg',
'https://www.youtube.com/watch?v=BGHGZjDguqw')

wonder = media.Movie('Wonder',
'The incredibly inspiring and heartwarming story of August Pullman, a boy with facial differences who enters fifth grade',
'https://m.media-amazon.com/images/M/MV5BYjFhOWY0OTgtNDkzMC00YWJkLTk1NGEtYWUxNjhmMmQ5ZjYyXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_QL50_SY1000_CR0,0,648,1000_AL_.jpg',
'https://www.youtube.com/watch?v=ngiK1gQKgK8')

justice_league = media.Movie('Justice League',
'As new enemies arise Batman, Wonder Woman, the Flash, Cyborg, and Aquaman must form the well known alliance Justice League to save the world ',
'https://pre00.deviantart.net/a4fe/th/pre/i/2017/330/2/a/justice_league_final_poster_by_everan614-dbukgll.jpg',
'https://www.youtube.com/watch?v=3cxixDgHUYw')

big_hero = media.Movie('Big Hero 6',
' Hiro and Baymax team up with four other nerds and save their hometown San Fransokyo',
'https://vignette.wikia.nocookie.net/disney/images/c/ca/Big_Hero_6_poster_2.jpg/revision/latest?cb=20140611014705',
'https://www.youtube.com/watch?v=8IdMPpKMdcc')

interstellar = media.Movie('Interstellar',
'Set in a future where a failing Earth puts humanity on the brink of extinction, it sees an intrepid team of NASA scientists, engineers and pilots attempt to find a new habitable planet, via interstellar travel.',
'http://fo4mw16y1z42edr6j2m4n6vt.wpengine.netdna-cdn.com/wp-content/uploads/interstellar-poster-655x1024.jpg',
'https://www.youtube.com/watch?v=zSWdZVtXT7E')

rockstar = media.Movie('Rockstar',
'College student Janardhan is a simpleton who desperately seeks inspiration for the musician inside him.',
'https://moviesposters.files.wordpress.com/2011/11/rockstar-2011nargis-fakiri.jpg',
'https://www.youtube.com/watch?v=bD5FShPZdpw')

#List to Store different Movie instances Created
movies = [spider_man,wonder,justice_league,big_hero,interstellar,rockstar]

#Creates an HTML page from the data provided
fresh_tomatoes.open_movies_page(movies)
