from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse


def index(request):
    return render(request, 'pizza_app/index.html')

def menu(request):
    return render(request, 'pizza_app/menu.html')