from home.models import MovieInfo

def get_movie_details(id: int):
    movie_info = MovieInfo.objects.get(movie_id=id)
    
    return movie_info