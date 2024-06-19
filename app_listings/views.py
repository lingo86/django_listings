from django.shortcuts import render
from .models import Listings

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')

def all_listings(request):
    listings = Listings.objects.order_by('-list_date')
    context = {'listings': listings}
    return render(request, 'listings/all_listings.html', context)
