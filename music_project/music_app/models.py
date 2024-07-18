from django.db import models
from datetime import datetime

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Track(models.Model):
    track_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Chart(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    rank = models.IntegerField()
    track_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.rank}: {self.track.name}'
