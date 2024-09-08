from django.shortcuts import render
from .utils import *

def detail(request, movie_id):
    details = get_movie_details(movie_id)

    return render(request, 'detail.html', context=details)