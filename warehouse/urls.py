from django.urls import path
from . import views

urlpatterns = [
    # Main page
    path('', views.warehouse, name='warehouse'),
    path('clients/', views.client, name='clients'),
    path('new-client/', views.addclient, name='new-client'),
]
