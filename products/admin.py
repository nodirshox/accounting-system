from django.contrib import admin
from .models import Product, Package, Micropackage, Packagesize, Packageprice


# Products
admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Micropackage)
admin.site.register(Packagesize)
admin.site.register(Packageprice)