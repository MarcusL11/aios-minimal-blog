from django.urls import path
from . import views

urlpatterns = [
    path("art_ai/", views.artgpt, name="artgpt"),
]

htmx_urlpatters = [
    path("generate_artwork/", views.generate_artwork, name="generate_artwork"),
]
urlpatterns += htmx_urlpatters
