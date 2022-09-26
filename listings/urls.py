from django.urls import path
from . import views 

urlpatterns = [
    path("action-adventure/", views.action_adventure, name="action-adventure"),
    path("comedies/", views.comedy, name='comedies'),
    path("blockbuster/", views.blockbuster, name="blockbuster"),
    path("drama/", views.drama, name="drama"),
    path("search/", views.search, name="search"),
    path("top10", views.top10, name="top10"),
    path("my_list", views.my_list, name="my-list"),
    path("my_list/add_to_my_list<int:id>", views.add_my_list, name="my_list"),
    path("<int:pk>", views.listing, name="listing")
]