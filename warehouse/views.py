from django.shortcuts import render
from . models import *
from django.contrib.auth.models import User, auth
# Create your views here.

# My warehouse
def warehouse(request):
    return render(request, 'warehouse.html')

# Clients
def client(request):
    clients = Client.objects.all()
    client_count = clients.count()
    context = {'clients': clients, 'client_count': client_count}
    return render(request, 'client/client.html', context)

def addclient(request):
    if request.user.is_authenticated:
        return render(request, 'client/new-client.html')
    else:
        #if request.method == 'POST':
        return render(request, 'client/new-client.html')

