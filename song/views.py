from django.shortcuts import render, get_object_or_404
from .models import Songlist, Song

def song_list(request, songlist_slug=None):
    songlist = None
    songlists = Songlist.objects.all()
    songs = Song.objects.filter(available=True)
    if songlist_slug:
        songlist = get_object_or_404(Songlist, slug=songlist_slug)
        songs = songs.filter(songlist=songlist)
    return render(request, 
                  'song/song/list.html', 
                  {'songlist': songlist, 
                  'songlists': songlists, 
                  'songs': songs})

def song_detail(request, id, slug):
    song = get_object_or_404(Song, id=id, slug=slug, available=True)
    return render(request,
                'song/song/detail.html',
                {'song': song})