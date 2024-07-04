from django.db import models

class MovieInfo(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=100, null=True)
    poster_path = models.CharField(max_length=100, null=True)
    genres = models.JSONField(null=True)
    popularity = models.FloatField(null=True)
    overview = models.CharField(max_length=1000, null=True)
    release_date = models.DateField(null=True)
    runtime = models.IntegerField()
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)