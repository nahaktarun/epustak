


from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

 
urlpatterns = [
      path('', views.books, name='books'),
      path('category/<slug:category_slug>/', views.books, name="books_by_category"),
      path('category/<slug:category_slug>/<slug:book_slug>/', views.read_books, name="read_books"),
      path('search/', views.search,name="search"),
      
 ]
 