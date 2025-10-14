from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) # Indexed for faster lookups
    slug = models.SlugField(max_length=100, unique=True) # URL-friendly identifier and unique, because no two categories should have the same slug

    class Meta:
        verbose_name_plural = 'categories' # To display the plural form correctly in the admin interface

    def __str__(self):
        
        return self.name