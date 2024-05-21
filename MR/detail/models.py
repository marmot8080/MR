from django.db import models
from home.models import MovieInfo
import json

class MovieInfo(models.Model):
    movie_id = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    plot = models.CharField(max_length=1000)
    rate = models.IntegerField()
    director = models.CharField(max_length=50)
    actors = models.JSONField()
    genres = models.JSONField()
    release_date = models.DateField(null=True)
    post_img_path = models.CharField(max_length=100)
    background_img_path = models.CharField(max_length=100)

    def get_actors(self):
        return json.loads(self.actors)
    
    def get_genres(self):
        return json.loads(self.genres)