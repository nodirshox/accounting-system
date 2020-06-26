from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('create-warehouse/', views.create_warehouse, name='create_warehouse'),
    
    # Clients
    path('clients/', views.client, name='clients'),
    path('client/create/', views.create, name='create_client'),
    path('client/update/<int:pk>/', views.update_client, name='update_client'),
    path('client/delete/<int:pk>/', views.delete_client, name='delete_client'),

    # Order
    path('order/create/', views.create_order, name='create_order'),
]
