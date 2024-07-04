from django.shortcuts import render
from .models import MovieInfo

def home(request):
    return render(request, 'home.html')