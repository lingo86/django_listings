from django.urls import path
from . import views

app_name = 'listings' # helps Django identify and choose the correct urls.py file from other urls.py files in the project’s directory

urlpatterns = [
    path("", views.index, name="index"),
    path("all_listings/", views.all_listings, name="all_listings"),
    path("new_listing/", views.new_listing, name="new_listing"),
]