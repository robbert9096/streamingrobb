from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name='about'),
    path("terms_of_use/", views.terms_of_use, name="terms-of-use")
]