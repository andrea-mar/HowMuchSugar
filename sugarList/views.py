from django.shortcuts import render
from sugarList.models import User, Product


def index(request):
    products = Product.objects.all()
    return render(request, 'sugarList/index.html', {
        'products': products,
    })
