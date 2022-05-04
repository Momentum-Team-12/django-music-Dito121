from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
    created = models.DateTimeField(auto_now_add=True)
    released = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

