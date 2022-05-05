from django.db import models
from django.conf import settings


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)
    created = models.DateTimeField(auto_now_add=True)
    released = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

