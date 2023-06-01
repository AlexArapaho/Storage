from django.shortcuts import render
from .models import Works


def index(request):
    projects = Works.objects.all()
    return render(request, 'works/index.html', {'projects': projects})
