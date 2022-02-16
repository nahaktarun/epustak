from django.urls import reverse
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from category.models import BookCategory
# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500,blank=True)
    book_cover_image = models.ImageField(upload_to='photos/books')
    pdf_file = models.FileField(upload_to="books/all_books",blank=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse('read_books', args=[self.category.slug, self.slug]) 
    
    def __str__(self):
        return self.book_name
    
    