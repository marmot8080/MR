from django.db import models

class MovieInfo(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    rate = models.IntegerField()
    release_date = models.DateField(null=True)
    post_img_path = models.CharField(max_length=100)