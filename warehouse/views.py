from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# My warehouse
@login_required(login_url='login')
def dashboard(request):
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

@login_required(login_url='login')
def create_warehouse(request):
    try:
        dashboard = Warehouse.objects.get(user=request.user)
        messages.info(request, 'You already have a dashboard.')
        return redirect('dashboard')
    except:
        if request.method == 'POST':
            form = WarehouseForm(request.POST or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.info(request, 'Congratulations, you just created dashboard.')
                return redirect('dashboard')
            else:
                return render(request, 'create_dashboard.html')
        else:
            form = WarehouseForm(request.POST or None)
            return render(request, 'create_dashboard.html', {'form': form})

# Clients
@login_required(login_url='login')
def all_clients(request):
    user = request.user
    warehouse = Warehouse.objects.get(user=user.id)
    clients = Client.objects.filter(warehouse=warehouse.id)
    return render(request, 'client/details.html', { 'clients': clients })

@login_required(login_url='login')
def create_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.warehouse = Warehouse.objects.get(user=request.user)
        obj.save()
        return redirect('all_clients')
    context = {
        'form': form
    }
    return render(request, 'client/create.html', context)

@login_required(login_url='login')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
    
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
# Orders
@login_required(login_url='login')
def all_orders(request):
    warehouse = Warehouse.objects.get(user=request.user)
    orders = Order.objects.filter(warehouse=warehouse.id)
    return render(request, 'order/details.html', { 'orders': orders })

@login_required(login_url='login')
def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.warehouse = Warehouse.objects.get(user=request.user)
        obj.save()
        return redirect('all_orders')

    return render(request, 'order/create.html', { 'form': form })

@login_required(login_url='login')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('all_orders')
    
    return render(request, 'client/create.html', { 'form': form })


# Payment
@login_required(login_url='login')
def all_payments(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, 'payment/details.html', context)

@login_required(login_url='login')
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
@login_required(login_url='login')
def all_recourses(request):
    recourses = Recourse.objects.all()
    context = {
        'recourses': recourses
    }
    return render(request, 'recourse/details.html', context)

@login_required(login_url='login')
def create_recourse(request):
    form = RecourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_recourses')
    context = {
        'form': form
    }
    return render(request, 'recourse/create.html', context)
