from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return render(request, 'pizza_app/index.html')

def index(request):
    return HttpResponse("Welcome to the Pizza App!")