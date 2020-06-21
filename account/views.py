from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from warehouse.models import Warehouse

# Main page
def home_page(request):
    return render(request, 'home_page.html')

# Authentication, Registration, Profile
def login(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.info(request, 'You have successfully logged in.')
                return redirect('/profile')
            else:
                messages.info(request, "Incorrect username or password.")
                return redirect('/login')
        else:
            return render(request, 'profile/login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, 'You have successfully logged out.')
        return redirect('/login')
    else:
        return redirect('/')

def registration(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == 'POST':
            full_name = request.POST['full_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            
            verified_profile = True
            if password != confirm_password:
                verified_profile = False
                messages.info(request, 'The passwords entered do not match.')
            if User.objects.filter(username=username).exists():
                verified_profile = False
                messages.info(request, 'Username taken.')
            if User.objects.filter(email=email).exists():
                verified_profile = False
                messages.info(request, 'Email taken.')
            if verified_profile:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=full_name)
                user.save()
                messages.info(request, 'Profile created, please sign in.')
                return redirect('/login')
            else:
                return redirect('/registration')

        else:
            return render(request, 'profile/registration.html')

def profile(request):
    current_user = request.user
    warehouse = Warehouse.objects.filter(owner=current_user.id)
    warehouse_count = warehouse.count()
    context = { 'warehouse': warehouse, 'warehouse_count': warehouse_count }

    if request.user.is_authenticated:
        return render(request, 'profile/profile.html', context)
    else:
        return redirect('/login')
