from django.shortcuts import render, get_object_or_404
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
    listing = get_object_or_404(Listing, pk=listing_id)
    photos = [getattr(listing, f'photo_{str(x + 1)}')
              for x in range(6)]
    return render(req, 'listings/listing.html', {'listing': listing, 'photos': photos})


def search(req):
    return render(req, 'listings/search.html')
