from django.shortcuts import render

# Create your views here.


def single_movie(request,pk):
    return render(request,"movies/single_movie.html")


def movies(request):
    return render(request, "movies/movies.html")