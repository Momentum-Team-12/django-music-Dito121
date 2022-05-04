from django.contrib import admin
from albums.models import Album


class AlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)
