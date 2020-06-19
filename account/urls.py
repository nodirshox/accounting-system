from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.mainpage, name='Main page'),

    # Profile path
    path('registration', views.registration, name='Registration'),
    path('login', views.login, name='Login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='Profile'),
    
]
