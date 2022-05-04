from django.shortcuts import render, redirect, get_object_or_404
from albums.models import Album


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    context = {"album": album}
    return render(request, "albums/album_detail.html", context)

