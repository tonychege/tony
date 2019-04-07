from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=25)
    artist_name = models.CharField(max_length=30)
    album_type = models.CharField(max_length=10)
    album_cover = models.FileField()


    def get_absolute_url(self):
        return reverse('musa:index', args=[str(self.pk)])

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=25)
    song_audio = models.FileField()
