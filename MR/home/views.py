from django.shortcuts import render
from .utils import *

def home(request):

    movie_info = {
        'recent_movies': get_recent_popular_movie_list(),
    }

    return render(request, 'home.html', {'movie_info': movie_info})