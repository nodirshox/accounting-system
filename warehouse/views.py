from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import ClientFilter
from .models import *
from .forms import *
from account.models import Currency

ITEMS_PER_PAGE = 10

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    try:
        warehouse = Warehouse.objects.get(user=request.user.id)
        clients = Client.objects.filter(warehouse=warehouse.id)
        total_clients = clients.count()
        orders = Order.objects.filter(warehouse=warehouse.id)
        total_orders = orders.count()
        context = { 'total_clients': total_clients, 'total_orders': total_orders }
        return render(request, 'dashboard/main.html', context)
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
            form = WarehouseForm(request.POST or None)
            return render(request, 'dashboard/create.html', {'form': form})

# Clients
@login_required(login_url='login')
def all_clients(request):
    warehouse = Warehouse.objects.get(user=request.user.id)
    clients = Client.objects.filter(warehouse=warehouse.id)

    myFilter = ClientFilter(request.GET, queryset=clients)
    clients = myFilter.qs

    return render(request, 'client/all.html', { 'clients': clients, 'myFilter': myFilter })

@login_required(login_url='login')
def create_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.warehouse = Warehouse.objects.get(user=request.user)
        obj.save()
        messages.info(request, 'Client successfully created.')
        return redirect('all_clients')

    return render(request, 'client/create.html', { 'form': form })

@login_required(login_url='login')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    user_warehouse = Warehouse.objects.get(user=request.user)

    if user_warehouse != client.warehouse:
        messages.info(request, 'You are not authorized to view this page.')
        return redirect('404')
    else:
        form = ClientForm(instance=client)

        if request.method == 'POST':
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                messages.info(request, 'Client successfully updated.')
                return redirect('client_detail', pk=client.id, )
        
        return render(request, 'client/update_client.html', { 'form': form, 'client_id': pk })

@login_required(login_url='login')
def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    user_warehouse = Warehouse.objects.get(user=request.user)

    if user_warehouse != client.warehouse:
        messages.info(request, 'You are not authorized to view this page.')
        return redirect('404')
    else:
        orders = Order.objects.filter(client=client).order_by('-date')
        return render(request,'client/detail.html', {'client': client, 'orders': orders})

@login_required(login_url='login')
def client_order(request, pk):
    client = Client.objects.get(id=pk)
    form = AddOrderClient()
    if request.method == 'POST':
        form = AddOrderClient(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.client = client
            obj.warehouse = client.warehouse
            obj.save()
            return redirect('/warehouse/client/detail/' + str(client.id))


    return render(request, 'client/order.html', { 'client': client, 'form': form })

@login_required(login_url='login')
def client_payment(request, pk):
    currency = Currency.objects.get(id=1)
    
    payments = Payment.objects.filter(order=pk)
    total_paid = 0
    for payment in payments:
        if payment.payment == 'bonus':
            total_paid += payment.money * currency.rate
        else:
            total_paid += payment.money

    order = Order.objects.get(id=pk)
    total_cost = order.product.cost * order.quantity
    
    status = None
    difference = 0
    if total_paid == total_cost:
        status = 'Paid'
    elif total_paid > total_cost:
        status = 'Over paid'
        difference = total_paid - total_cost
    else:
        status = 'Not paid'
        difference = total_cost - total_paid

    context = { 'payments': payments, 'order': order, 'total_paid': total_paid, 'status': status, 'difference': difference }
    return render(request, 'client/payment.html', context)

@login_required(login_url='login')
def client_payment_add(request, pk):
    form = AddPaymentClient()
    if request.method == 'POST':
        form = AddPaymentClient(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.order = Order.objects.get(id=pk)
            obj.save()
            return redirect('/warehouse/client/order/' + str(pk))

    return render(request, 'client/add_payment.html', {'form': form, 'order_id': pk})
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
    orders = Order.objects.filter(warehouse=warehouse.id).order_by('-date')
    
    paginator = Paginator(orders, ITEMS_PER_PAGE)
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'page_obj': page_obj, 'ITEMS_PER_PAGE': ITEMS_PER_PAGE }
    return render(request, 'order/details.html', context)

@login_required(login_url='login')
def create_order(request):
    warehouse = Warehouse.objects.get(user=request.user)
    form = OrderForm(warehouse, request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.warehouse = Warehouse.objects.get(user=request.user)
        obj.save()
        return redirect('all_orders')

    return render(request, 'order/create.html', { 'form': form })

@login_required(login_url='login')
def update_order(request, pk):
    warehouse = Warehouse.objects.get(user=request.user)
    order = Order.objects.get(id=pk)
    form = OrderForm(warehouse, instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('all_orders')
    
    return render(request, 'order/create.html', { 'form': form })


# Payment
@login_required(login_url='login')
def all_payments(request):
    payments = Payment.objects.all()
    return render(request, 'payment/details.html', { 'payments': payments })

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

@login_required(login_url='login')
def update_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    form = PaymentForm(instance=payment)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('all_payments')
    
    return render(request, 'payment/create.html', { 'form': form })

@login_required(login_url='login')
def delete_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    payment.delete()
    return redirect('/warehouse/client/order/' + str(payment.order.id))

# Recourse
@login_required(login_url='login')
def all_resources(request):
    warehouse = Warehouse.objects.get(user=request.user)
    resources = Resource.objects.filter(warehouse=warehouse).order_by('-date')
    

    paginator = Paginator(resources, ITEMS_PER_PAGE)
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = { 'page_obj': page_obj, 'ITEMS_PER_PAGE': ITEMS_PER_PAGE, 'resources': resources }
    return render(request, 'resource/details.html', context)


@login_required(login_url='login')
def create_resource(request):
    form = ResourceForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.warehouse = Warehouse.objects.get(user=request.user)
        obj.save()
        messages.info(request, "Resources added successfully.")
        return redirect('all_resources')

    return render(request, 'resource/create.html', { 'form': form })


@login_required(login_url='login')
def update_resource(request, pk):
    recourse = Resource.objects.get(id=pk)
    form = ResourceForm(instance=recourse)
    if request.method == 'POST':
        form = ResourceForm(request.POST or None)
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            return redirect('all_resources')
        else:
            print('a')

    return render(request, 'resource/update.html', {'form': form})
