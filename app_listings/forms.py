from django.forms import ModelForm
from .models import Listings

class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'condition', 'product_type', 'sale_type', 'price', 'main_photo', 'photo_1',
                   'contact_email', 'list_date', 'address']
