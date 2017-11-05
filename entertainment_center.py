import fresh_tomatoes
import media

pokemon_20 = media.Movie("Pokemon 20th - I Choose You!",
            "http://pokeshopper.com/Movie%2020/Ensky/"
            "movieposterartwork20hq4.jpg",
            "https://www.youtube.com/watch?v=r12w4iRBLp4")

pokemon_19 = media.Movie("Pokemon 19th - Volcanion and the Mechanical Marvel",
            "https://upload.wikimedia.org/wikipedia/en/8/85/Pok%C3%"
            "A9mon_movie_2016.png",
            "https://www.youtube.com/watch?v=uBJ7yENNbTE")

pokemon_18 = media.Movie("Pokemon 18th - Hoopa and the Clash of Ages",
            "https://c.76.my/Malaysia/pokemon-movie-18-hoopa-clash-ages-"
            "anime-movie-dvd-box-glauben-1610-19-glauben@37.jpg",
            "https://www.youtube.com/watch?v=bxTxlKvQFU8")

pokemon_17 = media.Movie("Pokemon 17th - Diancie and the Cocoon of Destruction",
            "http://www.beyondhe.com.au/media/catalog/product/cache/1/image/"
            "600x/040ec09b1e35df139433887a97daa66f/b/h/bhe5775-cover.jpg",
            "https://www.youtube.com/watch?v=v7SS33mFv5M")

pokemon_12 = media.Movie("Pokemon 12nd - Arceus and the Jewel of Life",
            "https://c.76.my/Malaysia/pokemon-movie-12-arceus-jewel-life-movie"
            "-box-set-glauben-1504-29-glauben@66.jpg",
            "https://www.youtube.com/watch?v=YWqh0EL6fqg")

pokemon_8 = media.Movie("Pokemon 8th - Lucario and the Mystery of Mew",
            "https://c.76.my/Malaysia/pokemon-movie-11-giratina-sky-warrior-"
            "movie-box-set-glauben-1504-29-glauben@65.jpg",
            "https://www.youtube.com/watch?v=cksY3fTkc_I")

pokemon_1 = media.Movie("Pokemon 1st - The First Movie",
            "http://vignette2.wikia.nocookie.net/toonami/images/9/9c/Pokemon_"
            "the_First_Movie.jpg/revision/latest?cb=20130913155508",
            "https://www.youtube.com/watch?v=o0eUE5TmBaM")

my_favorite_pokemon_movies = [pokemon_20, pokemon_19, pokemon_18, pokemon_17,
                              pokemon_12, pokemon_8, pokemon_1]

fresh_tomatoes.open_movies_page(my_favorite_pokemon_movies)
