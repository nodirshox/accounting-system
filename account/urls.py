from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.main_page, name='Main page'),

    # Profile path
    path('registration', views.registration, name='Registration'),
    path('login', views.login, name='Login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='Profile'),
    
    # Products
    path('products/', views.products, name='Products'),

    # Packages
    path('packages', views.packages, name='Packages'),
    path('packages/<int:id>', views.package, name='One package'),
    path('micropackage/<int:id>', views.micropackage, name='Micropackage')
]
