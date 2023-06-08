from django.shortcuts import render, redirect
from .models import Works
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback


def index(request):
    projects = Works.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'works/index.html', {'projects': projects, 'feedbacks': feedbacks})

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

@login_required()
def contacts(request):
    return render(request, 'works/contacts.html')

@login_required()
def feedback(request):
    if request.method == 'GET':
        return render(request, 'works/feedback.html', {'form': FeedbackForm()})
    else:
        try:
            form = FeedbackForm(request.POST)
            new_feed = form.save(commit=False)
            new_feed.user = request.user
            new_feed.save()
            return redirect('index')
        except ValueError:
            return render(request, 'works/feedback.html', {
                'form': FeedbackForm(),
                'error': 'Переданы неверные данные. Попробуйте еще раз'
            })
