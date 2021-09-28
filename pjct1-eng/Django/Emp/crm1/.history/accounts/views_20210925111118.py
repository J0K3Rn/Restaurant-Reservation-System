from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.



#____________________________________________________________________________
def home (request):
   return render(request, 'accounts/dashboard.htm')

def products (request):
   return render(request, 'accounts/products.htm')

def customer (request):
   return render(request, 'accounts/customer.htm')

def register (request):
   return render(request, 'accounts/register.htm')

def login (request):
   return render(request, 'accounts/login.htm')