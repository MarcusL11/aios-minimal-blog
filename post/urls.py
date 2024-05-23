from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("", views.about, name="about"),
    path("build-in-public/", views.build_in_public, name="build_in_public"),
    path("pfp_change/", views.pfp_change, name="pfp_change"),
]
