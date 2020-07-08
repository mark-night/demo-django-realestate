from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from .choices import state_choices, price_choices, bedroom_choices


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
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    keywords = req.GET.get('keywords')
    if keywords:
        listings = listings.filter(description__icontains=keywords)

    city = req.GET.get('city')
    if city:
        listings = listings.filter(city__iexact=city)

    state = req.GET.get('state')
    if state:
        listings = listings.filter(state__iexact=state)

    bedrooms = req.GET.get('bedrooms')
    if bedrooms:
        listings = listings.filter(bedrooms__lte=bedrooms)

    price = req.GET.get('price')
    if price:
        listings = listings.filter(price__lte=price)

    # pagination
    paginator = Paginator(listings, 6)
    on_page = req.GET.get('page')
    page_listings = paginator.get_page(on_page)

    return render(req, 'listings/search.html', {
        'bedrooms': bedroom_choices.items(),
        'prices': price_choices.items(),
        'states': state_choices.items(),
        'listings': page_listings,
        'values': req.GET
    })
