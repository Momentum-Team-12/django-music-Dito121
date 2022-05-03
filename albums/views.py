from django.shortcuts import render, redirect, get_object_or_404
from albums.models import Album


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {'albums': albums})
