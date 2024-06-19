from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingsForm

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')

def all_listings(request):
    listings = Listings.objects.order_by('-list_date')
    context = {'listings': listings}
    return render(request, 'listings/all_listings.html', context)

def new_listing(request):
    if request.method != 'POST':
        form = ListingsForm()
    else:
        form = ListingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings:all_listings')

    context = {'form': form}
    return render(request, 'listings/new_listing.html', context)

