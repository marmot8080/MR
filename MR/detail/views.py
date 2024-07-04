from django.shortcuts import render
from home.models import MovieInfo

def detail(request, movie_id):
    return render(request, 'detail.html')