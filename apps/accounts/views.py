from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(req):
    if req.user and req.user.is_authenticated:
        return redirect('dashboard')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is None:
                messages.error(req, 'Login failed, please try again.')
                return render(req, 'accounts/login.html', {'values': req.POST})
            else:
                auth.login(req, user)
                return redirect('dashboard')
        else:
            return render(req, 'accounts/login.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        messages.success(req, 'You are now logged out.')
    return redirect('index')


def register(req):
    if req.method == 'POST':
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        password2 = req.POST.get('password2')
        if password != password2:
            messages.error(req, 'Passwords do not match.')
            return render(req, 'accounts/register.html', {'values': req.POST})
        elif User.objects.filter(username=username).exists():
            messages.error(req, 'Username has been taken.')
            return render(req, 'accounts/register.html', {'values': req.POST})
        elif User.objects.filter(email=email).exists():
            messages.error(req, 'Email has been registered.')
            return render(req, 'accounts/register.html', {'values': req.POST})
        else:
            User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            messages.success(
                req, 'Registration succeeded. You can now log in below.')
            return redirect('login')
    else:
        return render(req, 'accounts/register.html')


def dashboard(req):
    return render(req, 'accounts/dashboard.html')
