from django import forms
from django.forms import fields




from .models import Comment, Post, Images


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['content']



class ImageForm(forms.ModelForm):

    class Meta:
        model = Images 
        fields = ['image']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']