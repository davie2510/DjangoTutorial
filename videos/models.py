from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=250)
    studio = models.CharField(max_length=250)
    logo = models.CharField(max_length=1000)


class Actor(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
