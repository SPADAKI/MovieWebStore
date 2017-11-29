import MovieWebStore
import media

ThorRagnarok = media.Movies("Thor Ragnarok",
                                   "A Story of Thor's Sister",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                                   "https://youtu.be/ue80QwXMRHg")

avengersinfinity = media.Movies("Avengers Infinity War",
                                   "A Story of young Man who gets Bitten by a Spider",
                                   "https://images.moviepilot.com/images/c_limit,q_auto:good,w_600/yrykjuw9yijoqaf4rt9d/best-fan-made-avengers-infinity-wars-posters.jpg",
                                   "https://youtu.be/6ZfuNTqbHE8")
SpiderManHomeComing = media.Movies("Spider Man Home Coming",
                                   "A Story of young Man who gets Bitten by a Spider",
                                   "https://images-na.ssl-images-amazon.com/images/I/91hi1TaZnZL._SX342_.jpg",
                                   "https://youtu.be/U0D3AOldjMU")

TheDarkKnight = media.Movies("The Dark Knight",
                                   "A Story of Gotham City and Batman",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                   "https://youtu.be/kmJLuwP3MbY")
toyStory =media.Movies("Toy Story",
                          "A story of a boy whose toys come to life",
                          "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                          "https://youtu.be/KYz2wyBy3kc")

Avatar =media.Movies("Avatar",
                          "A story of a Marine on an Alien planet",
                          "http://feoamante.com/Movies/A/Avatar/avatar.jpg",
                          "https://youtu.be/5PSNL1qE6VY?t=41")




movies=[ThorRagnarok,avengersinfinity,SpiderManHomeComing,TheDarkKnight,toyStory,Avatar]
index.open_movies_page(movies)
