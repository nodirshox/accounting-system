from django.urls import path
from . import views

urlpatterns = [

    # Home page
    path('', views.home_page, name='home_page'),

    # Profile
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile')
    
]
