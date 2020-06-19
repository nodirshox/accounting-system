from django.contrib import admin
from .models import *


# Products
admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Micropackage)
admin.site.register(Packagesize)
admin.site.register(Packageprice)
admin.site.register(Currency)