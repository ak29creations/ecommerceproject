from django.shortcuts import render, redirect
from django.db.models import Q
from shop.models import Product


def search_results(request):
    query = None
    products = None
    if 'search' in request.GET:
        query = request.GET.get('search')
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if not query:
        return redirect('/')
    else:
        return render(request, 'search.html', {'query': query, 'products': products})
