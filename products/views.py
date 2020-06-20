from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import *
# Create your views here.


# Products

def products(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products})

# Packages

def packages(request):
    packages = Package.objects.all()
    return render(request, 'product/packages.html', {'packages': packages})

def package(request, id):
    one_package = Package.objects.get(id=id)
    filtered_micropackages = Micropackage.objects.filter(package=id)
    return render(request, 'product/one_package.html', {'package': one_package, 'micropackages': filtered_micropackages})

def micropackage(request, id):
    micropackage = Micropackage.objects.get(id=id)
    return render(request, 'product/micropackage.html', {'micropackage': micropackage})