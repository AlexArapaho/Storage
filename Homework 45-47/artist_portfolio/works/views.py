from django.shortcuts import render, redirect
from .models import Works
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
    projects = Works.objects.all()
    return render(request, 'works/index.html', {'projects': projects})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'works/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'works/signupuser.html', {'form': UserCreationForm()}, {'error': 'Такое имя уже существует'})

        else:
            return render(request, 'works/signupuser.html', {'form': UserCreationForm()}, {'error': 'Пароли не совпадают'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'works/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'works/loginuser.html', {'form': AuthenticationForm(), 'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect("index")

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')