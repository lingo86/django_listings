from django.urls import path
from .views import index

app_name = 'listings' # helps Django identify and choose the correct urls.py file from other urls.py files in the project’s directory

urlpatterns = [
    path("", index, name="index")
]