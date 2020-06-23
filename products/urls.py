from django.urls import path
from . import views

urlpatterns = [
    # Products
    path('products/', views.products, name='products'),
    
    # Packages
    path('packages/', views.packages, name='packages'),
    path('packages/<int:id>/', views.package, name='one_package'),
    path('pack/<int:id>/', views.pack, name='pack')
]
