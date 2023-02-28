import os
from django.shortcuts import render
from django.views.generic import CreateView
from musiclabsite.forms import AuthUserForm, RegisterUserForm
from .models import Song, Author, Album, Playlist, Single
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def authors(request):  # Страница всех исполнителей.
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'musiclabsite/authors.html', context)


def author(request, pk):  # Страница одного исполнителя.
    author = Author.objects.get(id=pk)
    albums = Album.objects.filter(author=author)
    singles = Single.objects.filter(author=author)
    context = {'author': author, 'albums': albums, 'singles': singles}
    return render(request, 'musiclabsite/author.html', context)


def album(request, pk):  # Страница альбома.
    album = Album.objects.get(id=pk)
    songs = Song.objects.filter(album=album)
    base_dir = os.path.dirname(os.path.abspath(__file__)).split('musiclabsite')[0]
    base_dir.replace('\\', '/')
    context = {'album': album, 'songs': songs}
    return render(request, 'musiclabsite/album.html', context)


def playlists(request):  # Страница всех плейлистов.
    playlists = Playlist.objects.all()
    context = {'playlists': playlists}
    return render(request, 'musiclabsite/playlists.html', context)


def account(request):  # Страница пользователя.
    return render(request, 'musiclabsite/account.html')


class Login(LoginView):  # Страница авторизации.
    template_name = 'musiclabsite/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('account')

    def get_success_url(self):
        return self.success_url


class Register(CreateView):  # Страница регистрации.
    model = User
    template_name = 'musiclabsite/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class Logout(LogoutView):  # Выход из профиля.
    next_page = reverse_lazy('login')
