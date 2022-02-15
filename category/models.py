from tabnanny import verbose
from django.db import models

# Create your models here.

class BookCategory(models.Model):
    category_name= models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    image_category = models.ImageField(upload_to='photos/categories/', blank=True)
    
    
    def __str__(self):
        return self.category_name