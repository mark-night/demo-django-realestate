from django.shortcuts import render
from apps.listings.models import Listing
from apps.realtors.models import Realtor
from apps.listings.choices import bedroom_choices, state_choices, price_choices


def index(req):
    latests = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    return render(req, 'pages/index.html', {
        'latests': latests,
        'bedrooms': bedroom_choices.items(),
        'prices': price_choices.items(),
        'states': state_choices.items()
    })


def about(req):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = list(filter(lambda x: x.is_mvp, realtors))[0]
    return render(req, 'pages/about.html', {'realtors': realtors, 'mvp': mvp})
