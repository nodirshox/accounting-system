from django.contrib import admin
from .models import *


# Products
admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Pack)
admin.site.register(Quantity)
admin.site.register(Price)
