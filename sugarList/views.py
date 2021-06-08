from django.shortcuts import render
from sugarList.models import User, Product
from sugarList.forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, 'sugarList/index.html', {
        'products': products,
    })


def addproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            products = Product.objects.all()
            return render(request, 'sugarList/index.html', {
                'products': products,
            })
    return render(request, 'sugarList/addproduct.html', {
        'form': form
    })
