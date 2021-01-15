from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Listing


def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, per_page=6)
    page = request.GET.get('page', 1)
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)


def search(request):
    queryset_list = Listing.objects.order_by("-list_date")

    keywords = request.GET.get("keywords", None)
    if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
    city = request.GET.get("city", None)
    if city:
        queryset_list = queryset_list.filter(city__iexact=city)
    bedrooms = request.GET.get("bedrooms", None)
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    price = request.GET.get("price", None)
    if price:
        queryset_list = queryset_list.filter(price__lte=price)

    bedroom_choices = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10
    }

    price_choices = {
        '100000': '$100,000',
        '200000': '$200,000',
        '300000': '$300,000',
        '400000': '$400,000',
        '500000': '$500,000',
        '600000': '$600,000',
        '700000': '$700,000',
        '800000': '$800,000',
        '900000': '$900,000',
        '1000000': '$1M+',
    }

    state_choices = {

        'AB': 'abc',
        'CD': 'cde',
        'FG': 'fgh',
        'IJ': 'ijk',
        'LM': 'lmn',
        'OP': 'opq',
        'RS': 'rst',
        'UV': 'uvw',
        'XY': 'xyz'

    }

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'queryset_list': queryset_list
    }

    return render(request, 'listings/search.html', context)
