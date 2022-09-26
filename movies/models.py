from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User



# Create your models here.

category_movies = (
    ('Action & Adventure' , 'Action & Adventure'),
    ('Comedies', 'Comedies'),
    ('Drama' , 'Drama'),
    ('Blockbuster Movies', 'Blockbuster Movies'),
    ('Popular Movies', 'Popular Movies')
)

aged_restriction = (
    ('6+' , '6+'),
    ('12' , '12'),
    ('16' , '16'),
    ('18', '18')
)

tags = (
    ('Top10', 'Top10'),
    ('Exciting Movies', 'Exciting Movies'),
    ('Critically Acclaimed Films', 'Critically Acclaimed Films'),
    ('Familiar Favorites', 'Familiar Favorites'),
    ('Top10IMDb', "Top10IMDb")
)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    imdb = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    age_restriction = models.CharField(choices=aged_restriction, max_length=50, blank=True)
    category = models.CharField(choices=category_movies, max_length=100)
    tags = models.CharField(choices=tags, max_length=50)
    year_movie = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=205)
    main_image = models.ImageField(upload_to="main_photo/", blank=True)
    image = models.ImageField(upload_to="photos/")
    video = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    is_slider = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=datetime.now,blank=True)
    my_list = models.ManyToManyField(User, related_name="my_list", blank=True)

    def __str__ (self):
        return self.title

