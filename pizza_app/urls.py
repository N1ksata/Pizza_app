from django.urls import path
from . import views

ulrpatterns = [
    path('', views.home, name='home'),
]
