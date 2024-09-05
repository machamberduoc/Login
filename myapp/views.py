from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')  
        else:
            messages.error(request, 'Error al crear el usuario. Por favor, revisa los datos e intenta de nuevo.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'Username: {username}, Password: {password}')  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('welcome')
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtelo de nuevo.')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revise los campos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return redirect('login') 

def logout_view(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente')
    return redirect('login')  

def welcome(request):
    return render(request, 'welcome.html')  
