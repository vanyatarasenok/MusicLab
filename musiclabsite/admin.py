from django.contrib import admin
from . models import Song, Author, Album, Playlist, Single


@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'author', 'album', 'playlist']


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'url']


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'author']


@admin.register(Single)
class AdminSingle(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'author', 'file']


@admin.register(Playlist)
class AdminPlaylist(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
