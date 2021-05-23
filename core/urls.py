from django.urls import path
from .views import (home, 
                    post_list, 
                    delete_post, 
                    create_post, 
                    like_post, 
                    bookmark,
                    distroy_bookmark,
                    dislike_post, 
                    post_detail,
                    fav_list
                    )

urlpatterns = [
    path('', home, name="home"),
    path('post_list/', post_list, name="post_list"),
    path('posts/<int:id>/', post_detail, name="post_detail"),
    path('posts/bookmarks/', fav_list, name="bookmarks"),

    path('posts/create/', create_post, name="create_post"),
    path('posts/<int:id>/delete/', delete_post, name="delete_post"),

    #post like, dislike
    path('posts/<int:id>/like/', like_post, name="like_post"),
    path('posts/<int:id>/dislike/', dislike_post, name="dislike_post"),

    path('posts/<int:id>/bookmark/', bookmark, name="bookmark"),
    path('posts/<int:id>/distroy_bookmark/', distroy_bookmark, name="distroy_bookmark")
    #post like, dislike
]
