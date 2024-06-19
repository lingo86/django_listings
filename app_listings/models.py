from django.db import models
from django.utils.timezone import now

# Create your models here.

class Listings(models.Model):

    class ConditionType(models.TextChoices):
        USED = "used"
        NEW = "new"
    
    class ProductType(models.TextChoices):
        BIKE = "bike"
        PARTS = "parts"
        MODELS = "models"
        OTHERS = "others"

    class SaleType(models.TextChoices):
        PICK_UP = "Available for pickup"
        SHIP = "Available for shipping"

    title = models.CharField(max_length=100)
    condition = models.CharField(max_length=50, choices=ConditionType.choices, default=ConditionType.USED)
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.OTHERS)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.PICK_UP)
    price = models.FloatField()
    address = models.CharField(max_length=100)
    main_photo = models.ImageField()
    photo_1 = models.ImageField(blank=True)
    list_date = models.DateTimeField(default=now)
    #list_date = models.DateField(auto_now_add=True)
    contact_email = models.CharField(max_length=50)

    def __str__(self):
        """for admin panel"""
        return self.title
    
    class Meta:
        verbose_name_plural = "Listings"
