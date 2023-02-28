from django.urls import path
from musiclabsite import views
from musiclabsite.views import authors, author, album, playlists, account
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('authors/', authors, name='authors'),
    path('author/<int:pk>', author, name='author'),
    path('album/<int:pk>', album, name='album'),
    path('playlists/', playlists, name='playlists'),
    path('account/', account, name='account'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
