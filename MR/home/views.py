from django.shortcuts import render
from .utils import *

def home(request):

    # movie_info = {
    #     'recent_movies': get_recent_popular_movie_list(),
    #     'horror_movies': get_movie_list_by_genre(),
    #     'comedy_movies': get_movie_list_by_genre(),
    #     'animation_movies': get_movie_list_by_genre(),
    # }

    # 예시 값
    movie_info = {
        'recent_movies': [{'id': 1,
                           'title': 'a',
                          'image': '',
                          'rating': 3},
                          {'id': 2,
                           'title': 'b',
                          'image': '',
                          'rating': 4},
                          {'id': 3,
                           'title': 'c',
                          'image': '',
                          'rating': 2},
                          {'id': 4,
                           'title': 'd',
                          'image': '',
                          'rating': 1},
                          {'id': 1,
                           'title': 'a',
                          'image': '',
                          'rating': 3},
                          {'id': 2,
                           'title': 'b',
                          'image': '',
                          'rating': 4},
                          {'id': 3,
                           'title': 'c',
                          'image': '',
                          'rating': 2},
                          {'id': 4,
                           'title': 'd',
                          'image': '',
                          'rating': 1},
                          {'id': 1,
                           'title': 'a',
                          'image': '',
                          'rating': 3},
                          {'id': 2,
                           'title': 'b',
                          'image': '',
                          'rating': 4},
                          {'id': 3,
                           'title': 'c',
                          'image': '',
                          'rating': 2},
                          {'id': 4,
                           'title': 'd',
                          'image': '',
                          'rating': 1},],
    }

    return render(request, 'home.html', {'movie_info': movie_info})