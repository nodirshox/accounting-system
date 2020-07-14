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
    path('client/<int:pk>/', views.client_detail, name='client_detail'),

    # Order
    path('order/', views.all_orders, name='all_orders'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('order/<int:pk>/add_product/', views.add_product, name='add_product'),
    path('order/<int:pk>/create/', views.create_order, name='create_order'),
    path('order/<int:pk>/update/', views.update_order, name='update_order'),
    path('order/<int:pk>/deactivate/', views.deactivate_order, name="deactivate_order"),
    path('order/archived/', views.archived_orders, name="archived_orders"),

    #Payment
    path('payment/', views.all_payments, name='all_payments'),
    path('payment/order/<int:pk>/', views.client_payment, name='client_payment'),
    path('payment/order/create/<int:pk>/', views.create_payment, name='create_payment'),

    path('payment/update/<int:pk>/', views.update_payment, name='update_payment'),
    path('payment/delete/<int:pk>/', views.delete_payment, name='delete_payment'),

    #Resource
    path('resourse/details/', views.all_resources, name='all_resources'),
    path('resourse/create/', views.create_resource, name='create_resource'),
    path('resourse/update/<int:pk>/', views.update_resource, name='update_resource'),
    path('resource/delete/<int:pk>/', views.delete_resource, name='delete_resource')
]
