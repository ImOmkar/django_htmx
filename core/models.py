from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    bookmark = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content