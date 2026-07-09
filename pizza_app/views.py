from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pizza_app/index.html')

def menu(request):
    return render(request, 'pizza_app/menu.html')