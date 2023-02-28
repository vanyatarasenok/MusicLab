from django.db import models
from django.contrib.auth.models import AbstractUser


class Song(models.Model):  # Модель композиции.
    name = models.CharField(max_length=1000)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True)
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='audio/')

    def __str__(self):
        return self.name


class Author(models.Model):  # Модель исполнителя.
    name = models.CharField(max_length=100)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):  # Модель альбома.
    name = models.CharField(max_length=100)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Single(models.Model):  # Модель сингла.
    name = models.CharField(max_length=1000)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    file = models.FileField(blank=True, null=True, upload_to='audio/')

    def __str__(self):
        return self.name


class Playlist(models.Model):  # Модель плейлиста.
    name = models.CharField(max_length=100)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name
