from django.urls import path
from .views import (home, 
                    post_list, 
                    delete_post, 
                    create_post, 
                    like_post, 
                    dislike_post,
                    bookmark,
                    distroy_bookmark,
                    dislike_post, 
                    post_detail,
                    post_instance,
                    post_detail_like,
                    post_detail_dislike,
                    post_detail_distroy_bookmark,
                    post_detail_bookmark,
                    fav_list,
                    create_comment,
                    delete_comment,
                    comment_list
                    )


urlpatterns = [
    path('', home, name="home"),
    path('post_list/', post_list, name="post_list"),
    path('<slug:username>/status/<int:id>/', post_detail, name="post_detail"),
    path('post/<slug:username>/status/<int:id>/', post_instance, name="post_instance"),
    path('<slug:username>/status/<int:id>/detail_like_post', post_detail_like, name="post_detail_like"),
    path('<slug:username>/status/<int:id>/detail_dislike_post', post_detail_dislike, name="post_detail_dislike"),
    path('<slug:username>/bookmarks/', fav_list, name="bookmarks"),

    path('posts/create/', create_post, name="create_post"),
    path('posts/<slug:username>/<int:id>/delete/', delete_post, name="delete_post"),

    #post like, dislike
    path('posts/<slug:username>/<int:id>/like/', like_post, name="like_post"),
    path('posts/<slug:username>/<int:id>/dislike/', dislike_post, name="dislike_post"),

    path('posts/<slug:username>/<int:id>/bookmark/', bookmark, name="bookmark"),
    path('posts/<slug:username>/<int:id>/distroy_bookmark/', distroy_bookmark, name="distroy_bookmark"),
    path('posts/<slug:username>/<int:id>/detail_add_bookmark/', post_detail_bookmark, name="post_detail_bookmark"),
    path('posts/<slug:username>/<int:id>/detail_distroy_bookmark/', post_detail_distroy_bookmark, name="post_detail_distroy_bookmark"),
    #post like, dislike

    #comment
    path('posts/<slug:username>/<int:id>/comment_list/', comment_list, name="comment_list"),
    path('posts/<slug:username>/<int:id>/comment/create/', create_comment, name="create_comment"),
    path('posts/<slug:username>/<int:id>/comment_list/<int:pk>/delete_comment/', delete_comment, name="delete_comment"),

]
