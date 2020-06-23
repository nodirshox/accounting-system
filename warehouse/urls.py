from django.urls import path
from . import views

urlpatterns = [
    # Warehouse
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', views.client, name='clients'),
    path('client/create/', views.create, name='create_client'),
    path('client/update/<int:pk>/', views.update_client, name='update_client'),
    path('client/delete/<int:pk>/', views.delete_client, name='delete_client'),
]
