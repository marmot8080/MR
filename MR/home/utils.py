from .models import MovieInfo

def get_recent_popular_movie_list():
    latest_200_movies = MovieInfo.objects.order_by('-release_date')[:200]
    top_20_popular_movies = latest_200_movies.order_by('-popularity')[:20]

    return top_20_popular_movies

def get_movie_list_by_genre(genre: int):
    movie_list_by_genre = MovieInfo.objects.filter(genres__contains=[genre])

    latest_200_movies = movie_list_by_genre.order_by('-release_date')[:100]
    top_20_popular_movies = latest_200_movies.order_by('-popularity')[:20]

    return top_20_popular_movies