import json
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Post, Like


def api_add_like(request, id):
    data = json.loads(request.body)
    post_id = data['post_id']
    print(post_id)

    if not Like.objects.filter(id=post_id).filter(created_by=request.user).exists():
        like = Like.objects.create(id=post_id, created_by=request.user)
        post = Post.objects.get(id=post_id)

    return JsonResponse({'success': True})

