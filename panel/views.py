from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def main_page(request):
    return render(request, 'home_page.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Successfully signed')
            return redirect('/profile')
        else:
            messages.info(request, "Username or password incorrect")
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfully sign out')
    return redirect('/')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        verified_profile = True
        if password != confirm_password:
            verified_profile = False
            messages.info(request, 'Password not matching')
        if User.objects.filter(username=username).exists():
            verified_profile = False
            messages.info(request, 'Username taken')
        if User.objects.filter(email=email).exists():
            verified_profile = False
            messages.info(request, 'Email taken')
        if verified_profile:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.info(request, 'Profile createad, please log in...')
            return redirect('/login')
        else:
            return redirect('/registration')

    else:
        return render(request, 'registration.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/login')