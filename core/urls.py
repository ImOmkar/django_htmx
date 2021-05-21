from django.urls import path
from .views import (home, 
                    post_list, 
                    delete_post, 
                    create_post, 
                    like_post, 
                    favourite,
                    distroy_favourite,
                    dislike_post, 
                    post_detail,
                    )

urlpatterns = [
    path('', home, name="home"),
    path('post_list/', post_list, name="post_list"),

    path('posts/<int:id>/', post_detail, name="post_detail"),

    path('posts/create/', create_post, name="create_post"),
    path('posts/<int:id>/delete/', delete_post, name="delete_post"),

    #post like, dislike
    path('posts/<int:id>/like/', like_post, name="like_post"),
    path('posts/<int:id>/dislike/', dislike_post, name="dislike_post"),

    path('posts/<int:id>/favourite/', favourite, name="favourite"),
    path('posts/<int:id>/distroy_favourite/', distroy_favourite, name="distroy_favourite")
    #post like, dislike
]
