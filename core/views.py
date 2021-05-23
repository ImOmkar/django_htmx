from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm
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


def bookmark(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.add(request.user)
    return redirect('post_list')


def distroy_bookmark(request, id):
    post = get_object_or_404(Post, id=id)
    if post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.remove(request.user)
    return redirect('post_list')



def fav_list(request):
    user = request.user
    bookmarks = user.bookmark.all()
    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmarks.html', context)


    

