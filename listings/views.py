from django.shortcuts import render, get_object_or_404
from movies .models import Movie
from django.http import HttpResponseRedirect

# Create your views here.


def listing(request, pk):
    single_movie = get_object_or_404 (Movie, pk=pk)
    more_like_this = Movie.objects.order_by('-date_published')
    return render(request, 'listings/listing.html',{
        'movie' : single_movie,
        'more_like_this' : more_like_this
    })



def action_adventure(request):
    slider_movie = Movie.objects.order_by('-date_published').filter(category='Action & Adventure', is_slider=True, tags="Familiar Favorites")
    familiar_favorites = Movie.objects.order_by('-date_published').filter(tags="Familiar Favorites", category="Action & Adventure")
    exciting_movies = Movie.objects.order_by('-date_published').filter(tags="Exciting Movies", category="Action & Adventure")
    slider_1 = Movie.objects.filter(id=37)
    return render(request, "listings/action_adventure.html", {
        'slider_movie' : slider_movie,
        'exciting_movies' : exciting_movies,
        'familiar_favorites' : familiar_favorites,
        'slider_1' : slider_1
    })



def comedy(request):
    slider_movie = Movie.objects.order_by('-date_published').filter(category='Comedies', is_slider=True)
    familiar_favorites = Movie.objects.order_by('-date_published').filter(category="Comedies", tags="Familiar Favorites")
    exciting_movies = Movie.objects.order_by('-date_published').filter( category="Comedies", tags="Exciting Movies")
    return render(request, "listings/comedy.html", {
        'slider_movie' : slider_movie,
        'exciting_movies' : exciting_movies,
        'familiar_favorites' : familiar_favorites
    })



def blockbuster(request):
    slider_movie = Movie.objects.order_by('-date_published').filter(category='Blockbuster Movies', is_slider=True)
    familiar_favorites = Movie.objects.order_by('-date_published').filter(category="Blockbuster Movies", tags="Familiar Favorites")
    exciting_movies = Movie.objects.order_by('-date_published').filter( category="Blockbuster Movies", tags="Exciting Movies")
    return render(request, "listings/blockbuster.html", {
        'slider_movie' : slider_movie,
        'exciting_movies' : exciting_movies,
        'familiar_favorites' : familiar_favorites
    })

def drama(request):
    slider_movie = Movie.objects.order_by('-date_published').filter(category='Drama', is_slider=True)
    familiar_favorites = Movie.objects.order_by('-date_published').filter(category="Drama", tags="Familiar Favorites")
    exciting_movies = Movie.objects.order_by('-date_published').filter( category="Drama", tags="Exciting Movies")
    return render(request, "listings/drama.html", {
        'slider_movie' : slider_movie,
        'exciting_movies' : exciting_movies,
        'familiar_favorites' : familiar_favorites
    })


def search(request):
    queryset_list = Movie.objects.order_by('-date_published')
    # Keywords     
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords) 

    return render(request, "listings/search.html",{
        'exciting_movies' : queryset_list
    })


def top10(request):
    slider_movie = Movie.objects.order_by('-date_published').filter(tags="Top10IMDb", is_slider=True)
    popular_movies = Movie.objects.order_by('-date_published').filter(tags = "Top10IMDb")
    new_movies = Movie.objects.order_by('-date_published').filter( category="Drama")
    return render(request, "listings/top10imdb.html", {
        'slider_movie' : slider_movie,
        'new_movies' : new_movies,
        'popular_movies' : popular_movies
    })
    return render(request,"listings/top10imdb.html")



def add_my_list(request, id):
    item = get_object_or_404(Movie, id=id)
    if item.my_list.filter(id=request.user.id).exists():
        item.my_list.remove(request.user)
    else:
        item.my_list.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
    

def my_list(request):
    item = Movie.objects.filter(my_list=request.user)
    return render(request, "listings/my_list.html",{
        'my_list' : item
    })