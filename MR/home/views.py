from django.shortcuts import render
from .utils import *

def home(request):

    context = {
        'recent_movies': get_recent_popular_movie_list(),
        'horror_movies': get_movie_list_by_genre(),
        'comedy_movies': get_movie_list_by_genre(),
        'animation_movies': get_movie_list_by_genre(),
    }

    return render(request, 'home.html', context)