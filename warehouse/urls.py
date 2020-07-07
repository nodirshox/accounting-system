from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('create-warehouse/', views.create_warehouse, name='create_warehouse'),
    
    # Clients
    path('client/', views.all_clients, name='all_clients'),
    path('client/create/', views.create_client, name='create_client'),
    path('client/update/<int:pk>/', views.update_client, name='update_client'),
    path('client/detail/<int:pk>/', views.client_detail, name='client_detail'),
    path('client/order/<int:pk>/', views.client_payment, name='client_payment'),
    path('client/order/payment/<int:pk>/', views.client_payment_add, name='client_payment_add'),

    # Order
    path('order/', views.all_orders, name='all_orders'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/create/<int:pk>/', views.client_order, name='client_order'),
    path('order/update/<int:pk>/', views.update_order, name='update_order'),

    #Payment
    path('payment/', views.all_payments, name='all_payments'),
    path('payment/create/', views.create_payment, name='create_payment'),
    path('payment/update/<int:pk>/', views.update_payment, name='update_payment'),

    #Resource
    path('resourse/details/', views.all_resources, name='all_resources'),
    path('resourse/create/', views.create_resource, name='create_resource'),
    path('resourse/update/<int:pk>/', views.update_resource, name='update_resource')
]
