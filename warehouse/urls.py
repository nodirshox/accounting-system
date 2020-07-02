from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('create-warehouse/', views.create_warehouse, name='create_warehouse'),
    
    # Clients
    path('clients/', views.all_clients, name='all_clients'),
    path('client/create/', views.create_client, name='create_client'),
    path('client/update/<int:pk>/', views.update_client, name='update_client'),

    # Order
    path('order/create/', views.create_order, name='create_order'),
    path('orders/', views.all_orders, name='all_orders'),

    #Payment
    path('payment/', views.all_payments, name='all_payments'),
    path('payment/create/', views.create_payment, name='create_payment'),

    #Recourses
    path('recourse/details/', views.all_recourses, name='all_recourses'),
    path('recource/create/', views.create_recourse, name='create_recourse')
]
