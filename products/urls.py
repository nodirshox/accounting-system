from django.urls import path
from . import views

urlpatterns = [
    # Products
    path('', views.products, name='Products'),
    # Packages
    path('packages', views.packages, name='Packages'),
    path('packages/<int:id>', views.package, name='One package'),
    path('micropackage/<int:id>', views.micropackage, name='Micropackage')
]
