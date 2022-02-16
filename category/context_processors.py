from .models import BookCategory
 
def menu_links(request):
    links = BookCategory.objects.all()
    return dict(links=links)
 