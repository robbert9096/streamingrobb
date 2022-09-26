from django.shortcuts import render
from movies .models import Movie
# Create your views here.

def home(request):
    action_movie = Movie.objects.order_by('-date_published').filter(category ='Action & Adventure')
    comedy_movie = Movie.objects.order_by('-date_published').filter(category = 'Comedies')
    block_buster = Movie.objects.order_by(('-date_published')).filter(category = 'Blockbuster Movies')
    top_10 = Movie.objects.order_by('-date_published').filter(tags='Top-10')
    drama_movies = Movie.objects.order_by('-date_published').filter(category = 'Drama')
    last_movies = Movie.objects.order_by('-date_published')[0:3]
    return render(request, 'pages/home.html',{
        'movie' : action_movie,
        'comedy_movies' : comedy_movie,
        'block_buster' : block_buster,
        'top_10' : top_10,
        'dramas_movies' : drama_movies,
        'last_movies' : last_movies,
        
    })


def about(request):
    return render(request, 'pages/about.html')


def terms_of_use(request):
    return render(request,"pages/terms_of_use.html")