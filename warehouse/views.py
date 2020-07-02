from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# My warehouse
def dashboard(request):
    if request.user.is_authenticated:
        try:
            warehouse = Warehouse.objects.get(user=request.user.id)
            clients = Client.objects.filter(warehouse=warehouse.id)
            total_clients = clients.count()
            orders = Order.objects.filter(warehouse=warehouse.id)
            total_orders = orders.count()
            context = { 'clients': clients, 'total_clients': total_clients, 'cash': warehouse.cash, 'terminal': warehouse.terminal, 'bonus': warehouse.bonus, 'orders': orders, 'total_orders': total_orders }
            return render(request, 'dashboard.html', context)
        except:
            messages.info(request, 'Please, press button below to create warehouse.')
            return redirect('create_warehouse')
    else:
        return redirect('login')

def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'create_warehouse.html')
    else:
        initial_data = {
            'user': request.user
        }
        form = WarehouseForm(request.POST or None, initial=initial_data)
        return render(request, 'create_warehouse.html', {'form': form})
# Clients
def all_clients(request):
    if request.user.is_authenticated:        
        user = request.user
        warehouse = Warehouse.objects.get(user=user.id)
        clients = Client.objects.filter(warehouse=warehouse.id)
        client_count = clients.count()
        
        context = { 'clients': clients, 'client_count': client_count }

        return render(request, 'client/all_clients.html', context)
    else:
        return redirect('/login')

def create_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        form.warehouse = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = { 'form': form }    
    return render(request, 'client/create.html', context)

def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/warehouse/clients')
    
    context = { 'form': form }
    return render(request, 'client/create.html', context)
"""
def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/warehouse/clients')
    context = { 'client': client }
    return render(request, 'client/delete_client.html', context)
"""

def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_orders')

    context = {
        'form': form
    }    
    return render(request, 'order/create.html', context)

def all_orders(request):
    warehouse = Warehouse.objects.get(user=request.user)
    orders = Order.objects.filter(warehouse=warehouse.id)

    context = { 'orders': orders }
    return render(request, 'order/all_orders.html', context)

# Payment

def all_payments(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'payment/details.html', context)

def create_payment(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_payments')
    context = {
        'form': form
    }
    return render(request, 'payment/create.html', context)

# Recourse
def all_recourses(request):
    recourses = Recourse.objects.all()
    context = {
        'recourses': recourses
    }
    return render(request, 'recourse/details.html', context)

def create_recourse(request):
    form = RecourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_recourses')
    context = {
        'form': form
    }
    return render(request, 'recourse/create.html', context)
