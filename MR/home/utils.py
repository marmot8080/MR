from .models import MovieInfo

def get_recent_popular_movie_list():
    top_20_popular_movies = MovieInfo.objects.all().order_by('-release_date', '-popularity')[:200][:20]

    return top_20_popular_movies

def get_movie_list_by_genre(genre: int):
    movie_list_by_genre = MovieInfo.objects.all().filter(genres__contains=[genre])
    top_20_popular_movies = movie_list_by_genre.order_by('-release_date', '-popularity')[:200][:20]

    return top_20_popular_movies