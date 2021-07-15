import django
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment, Images
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.

@login_required
def home(request):

    form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'home.html', context)


@login_required
def post_list(request):
    posts = Post.objects.all()
    comment_count = Post.objects.annotate(no_of_cmt=Count('comment'))
    context = {
        'posts': posts,
        'comment_count': comment_count
    }
    return render(request, "post_list.html", context)


@login_required
def create_post(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        img_file = request.FILES.getlist("filepond")
        if postform.is_valid():
            post_form = postform.save(commit=False)
            post_form.author = request.user
            post_form.save()
            for f in img_file:
                photo = Images(post=post_form, image=f)
                photo.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create_post.html', context)



@login_required
def delete_post(request, id, **kwargs):
    Post.objects.filter(id=id, author__username=kwargs['username']).delete()
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)



def post_instance(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    context = {
        'post': post,
    }
    return render(request, 'post_instance.html', context)


def post_detail(request, id, *args, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    form = CommentForm()
    
    context = {
        'form': form,
        'post': post
    }

    return render(request, 'post_detail.html', context)



@login_required
def create_comment(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
    else:
        form = CommentForm()
    return redirect('post_detail', username=kwargs['username'], id=id)



def comment_list(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    comments = Comment.objects.filter(post=post).order_by('-timestamp')

    context = {
        'post': post,
        'comments': comments
    }
    return render(request, "comment_list.html", context)


def delete_comment(request, id, pk, **kwargs):
    Comment.objects.filter(id=pk).delete()
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    return redirect('comment_list', username=kwargs['username'], id=id)



@login_required
def fav_list(request, **kwargs):
    user = request.user
    bookmarks = user.bookmark.all()
    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmarks.html', context)


    






#multiple func to enable like, bookmark on different pages.

#like/dislike to feed page
@login_required
def like_post(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if not post.likes.filter(id=request.user.id).exists():
        post.likes.add(request.user)
    return redirect('post_list')

@login_required
def dislike_post(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    return redirect('post_list')


#bookmark/distroy to feed page
@login_required
def bookmark(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if not post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.add(request.user)
    return redirect('post_list')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def distroy_bookmark(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.remove(request.user)
    return redirect('post_list')


#like/dislike to detail page
@login_required
def post_detail_like(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if not post.likes.filter(id=request.user.id).exists():
        post.likes.add(request.user)
    return redirect('post_detail', username=kwargs['username'], id=id)

@login_required
def post_detail_dislike(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    return redirect('post_detail', username=kwargs['username'], id=id)


#bookmark/distroy to detail feed
@login_required
def post_detail_bookmark(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if not post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.add(request.user)
    return redirect('post_detail', username=kwargs['username'], id=id)

@login_required
def post_detail_distroy_bookmark(request, id, **kwargs):
    post = get_object_or_404(Post, id=id, author__username=kwargs['username'])
    if post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.remove(request.user)
    return redirect('post_detail', username=kwargs['username'], id=id)
