from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','category','created_date','modified_date')
    prepopulated_fields = {'slug': ('book_name',)}

admin.site.register(Book, BookAdmin)
