from django.contrib import admin
from .models import Product, Package, Micropackage, Packagetype

# Register your models here.

admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Micropackage)
admin.site.register(Packagetype)