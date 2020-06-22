from django.urls import path
from . import views

urlpatterns = [
    # Warehouse
    path('warehouse/', views.my_warehouse, name='warehouse'),
    path('clients/', views.client, name='clients'),
    path('new_client/', views.add_client, name='new_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
]
