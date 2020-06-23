from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import *
# Create your views here.


# Products
def products(request):
    products = Product.objects.all()
    context = { 'products': products }

    return render(request, 'product/products.html', context)

# Packages
def packages(request):
    packages = Package.objects.all()
    context = { 'packages': packages }

    return render(request, 'product/packages.html', context)

def package(request, id):
    package = Package.objects.get(id=id)
    packs = Pack.objects.filter(package=id)
    context = { 'package': package, 'packs': packs }

    return render(request, 'product/one_package.html', context)

def pack(request, id):
    pack = Pack.objects.get(id=id)
    products = Quantity.objects.filter(pack=id)
    context = { 'pack': pack, 'products': products }

    return render(request, 'product/pack.html', context)