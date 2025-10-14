from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) # Indexed for faster lookups
    slug = models.SlugField(max_length=100, unique=True) # URL-friendly identifier and unique, because no two categories should have the same slug

    class Meta:
        verbose_name_plural = 'categories' # To display the plural form correctly in the admin interface

    def __str__(self):

        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # Foreign key to Category model, with related name 'products' for reverse lookups
    name = models.CharField(max_length=200, db_index=True) # Indexed for faster lookups
    slug = models.SlugField(max_length=200, db_index=True) # URL-friendly identifier
    description = models.TextField(blank=True) # Optional field for product description
    price = models.DecimalField(max_digits=10, decimal_places=2) # Decimal field for price with two decimal places
    available = models.BooleanField(default=True) # Boolean field to indicate if the product is available
    image = models.ImageField(upload_to='images/', blank=True) # Optional image field, images will be uploaded to a date-based directory structure

    class Meta:
        verbose_name_plural = 'products' # Plural name for admin interface

    def __str__(self):
        return self.name