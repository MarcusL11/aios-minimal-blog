from django.urls import path
from . import views

urlpatterns = [
    path("art_ai/", views.artgpt, name="artgpt"),
]

htmx_urlpatters = [
    path("generate_artwork/", views.generate_artwork, name="generate_artwork"),
    path("artwork_modal/", views.artwork_modal, name="artwork_modal"),
]
urlpatterns += htmx_urlpatters
