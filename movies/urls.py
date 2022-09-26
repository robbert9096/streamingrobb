from django.urls import path 
from . import views

urlpatterns = [
    path("", views.movies, name="movies"),
    path("<int:pk>", views.single_movie, name="single-movie")
]