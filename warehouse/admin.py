from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Warehouse)
admin.site.register(Resource)
admin.site.register(Order)
admin.site.register(Payment)