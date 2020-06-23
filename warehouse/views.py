from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User, auth
from . forms import ClientForm
# My warehouse
def my_warehouse(request):
    if request.user.is_authenticated:
        return render(request, 'warehouse.html')
    else:
        return redirect('/login')
# Clients
def client(request):
    if request.user.is_authenticated:        
        user = request.user
        warehouse = Warehouse.objects.get(owner=user.id)
        clients = Client.objects.filter(warehouse=warehouse.id)
        client_count = clients.count()
        
        context = { 'clients': clients, 'client_count': client_count }

        return render(request, 'client/client.html', context)
    else:
        return redirect('/login')
def add_client(request):

    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/warehouse/clients')
    context = { 'form': form }    
    return render(request, 'client/new_client.html', context)

def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/warehouse/clients')
    
    context = { 'form': form }
    return render(request, 'client/new_client.html', context)

def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/warehouse/clients')
    context = { 'client': client }
    return render(request, 'client/delete_client.html', context)

