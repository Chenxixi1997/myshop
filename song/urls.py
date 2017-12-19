from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.song_list, name='song_list'),
    url(r'^(?P<songlist_slug>[-\w]+)/$', views.song_list, name='song_list_by_songlist'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.song_detail, name='song_detail'),
]

