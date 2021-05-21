from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.urls import reverse
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'home.html', context)



def post_list(request):
    posts = Post.objects.all()

    context = {

        'posts': posts,
    }
    return render(request, "post_list.html", context)



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'tasks_create.html', context)



def delete_post(request, id):
    Post.objects.filter(id=id).delete()
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post
    }

    return render(request, 'post_detail.html', context)


def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.likes.filter(id=request.user.id).exists():
        post.likes.add(request.user)
    return redirect('post_list')


def dislike_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    return redirect('post_list')


def favourite(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.favourite.filter(id=request.user.id).exists():
        post.favourite.add(request.user)
    return redirect('post_list')


def distroy_favourite(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    return redirect('post_list')





    

