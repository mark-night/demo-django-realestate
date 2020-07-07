from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing


def index(req):
    # '-' changes the order type to descendent
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # pagination
    paginator = Paginator(listings, 6)
    on_page = req.GET.get('page')
    page_listings = paginator.get_page(on_page)
    return render(req, 'listings/listings.html', {'listings': page_listings})


def listing(req, listing_id):
    return render(req, 'listings/listing.html')


def search(req):
    return render(req, 'listings/search.html')
