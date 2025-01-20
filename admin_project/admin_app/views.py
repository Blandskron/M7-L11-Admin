from django.shortcuts import render, redirect
from .models import Gasto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login exitoso')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout exitoso')
    return redirect('login')

def home(request):
    gastos = Gasto.objects.all()
    return render(request, 'home.html', {'gastos': gastos})
