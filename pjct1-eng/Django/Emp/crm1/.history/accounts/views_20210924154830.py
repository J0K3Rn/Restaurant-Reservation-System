from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
   return render(request, 'accounts/dashboard.htm')

def products (request):
   return render(request, 'accounts/products.htm')

def customer (request):
   return render(request, 'accounts/customer.htm')

def register (request):
   return render(request, 'accounts/register.htm')