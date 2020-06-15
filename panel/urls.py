from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Main page'),

    # Profile path
    path('registration', views.registration, name='Registration'),
    path('login', views.login, name='Login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='Profile')
    
]
