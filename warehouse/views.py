from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import ClientFilter
from .models import *
from .forms import *
from account.models import Currency
from products.models import Pack

ITEMS_PER_PAGE = 5

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    try:
        warehouse = Warehouse.objects.get(user=request.user.id)
        clients = Client.objects.filter(warehouse=warehouse.id)
        total_clients = clients.count()
        orders = Order.objects.all()
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
    clients = Client.objects.filter(warehouse=warehouse.id).order_by('-date')

    myFilter = ClientFilter(request.GET, queryset=clients)
    clients = myFilter.qs

    paginator = Paginator(clients, ITEMS_PER_PAGE)
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = { 'page_obj': page_obj, 'ITEMS_PER_PAGE': ITEMS_PER_PAGE, 'myFilter': myFilter, 'clients': clients }
    return render(request, 'client/all_clients.html', context)

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
        return render(request, 'client/update.html', { 'form': form, 'client_id': pk })

@login_required(login_url='login')
def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    user_warehouse = Warehouse.objects.get(user=request.user)

    if user_warehouse != client.warehouse:
        messages.info(request, 'You are not authorized to view this page.')
        return redirect('404')
    else:
        orders = Order.objects.filter(client=client).order_by('-date')
        myFilter = ClientFilter(request.GET, queryset=orders)
        clients = myFilter.qs

        paginator = Paginator(clients, ITEMS_PER_PAGE)
        page_number  = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
        context = { 'page_obj': page_obj, 'ITEMS_PER_PAGE': ITEMS_PER_PAGE, 'myFilter': myFilter, 'client': client, 'orders': orders }
        return render(request,'client/detail.html', context)

# Orders
@login_required(login_url='login')
def all_orders(request):
    orders = Order.objects.all().order_by('-date')
    
    paginator = Paginator(orders, ITEMS_PER_PAGE)
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'page_obj': page_obj, 'ITEMS_PER_PAGE': ITEMS_PER_PAGE }
    return render(request, 'order/details.html', context)


@login_required(login_url='login')
def create_order(request, pk):
    products = Product.objects.all()
    pack = Pack.objects.all()
    client = Client.objects.get(id=pk)

    print(client.warehouse)
    warehouse = Warehouse.objects.get(user=request.user)
    print(warehouse)
    if client.warehouse == warehouse:
        if request.method == 'POST':
            product_id = request.POST['product']
            quantity = request.POST['quantity']

            product = Product.objects.get(id=product_id)
            my_data = Order(client=client, product=product.name, price=product.product_price * int(quantity), quantity=quantity, detail=quantity + 'x, ' + product.name + ', ' + str(product.product_price))
            my_data.save()
            messages.info(request, 'Order added successfully.')
            return redirect('/warehouse/client/' + str(client.id))

        return render(request, 'order/create.html', { 'products': products, 'pack': pack, 'client': client })
    else:
        messages.info(request, 'You are not authorized to view this page.')
        return redirect('404')
    

# Fix this
@login_required(login_url='login')
def update_order(request, pk):
    pass

# Payment
@login_required(login_url='login')
def all_payments(request):
    payments = Payment.objects.all()
    return render(request, 'payment/details.html', { 'payments': payments })

@login_required(login_url='login')
def client_payment(request, pk):
    currency = Currency.objects.get(id=1)
    
    payments = Payment.objects.filter(order=pk).order_by('-date')
    total_paid = 0
    for payment in payments:
        if payment.payment == 'bonus':
            total_paid += payment.money * currency.rate
        else:
            total_paid += payment.money
    order = Order.objects.get(id=pk)

    total_cost = order.price
    
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
    return render(request, 'payment/order_payment.html', context)

@login_required(login_url='login')
def create_payment(request, pk):
    form = AddPaymentClient()
    if request.method == 'POST':
        form = AddPaymentClient(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.order = Order.objects.get(id=pk)
            obj.save()
            messages.info(request, "Payment successfully added.")
            return redirect('/warehouse/payment/order/' + str(pk))

    return render(request, 'payment/create.html', {'form': form, 'order_id': pk})


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
    return redirect('/warehouse/payment/order/' + str(payment.order.id))

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
    resource = Resource.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST.get('quantity').isnumeric():
            resource.quantity = request.POST.get('quantity')
            resource.save()
            messages.info(request, 'Resource successfully updated.')
            return redirect('all_resources')
        else:
            messages.info(request, 'Please enter only positive number.')
            return redirect('all_resources')

    return render(request, 'resource/update.html', { 'resource': resource })

@login_required(login_url='login')
def delete_resource(request, pk):
    resource = Resource.objects.get(id=pk)
    if resource.warehouse == Warehouse.objects.get(user=request.user):
        if request.method == 'POST':
            resource.delete()
            messages.info(request, 'Resources deleted successfully.')
            return redirect('all_resources')
    else:
        messages.info(request, 'You are not authorized to view this page.')
        return redirect('404')

    return render(request, 'resource/delete.html', {'resource': resource})
