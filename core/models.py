from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.fields import TextField
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    bookmark = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmark', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content



class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", blank=True, null=True)


    def __str__(self):
        return self.post.content



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content