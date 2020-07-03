from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('404/', views.not_found, name='404' )
]
