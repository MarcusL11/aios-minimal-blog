from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("posts/", views.post_list, name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),
    path("build-in-public/", views.build_in_public, name="build_in_public"),
]
