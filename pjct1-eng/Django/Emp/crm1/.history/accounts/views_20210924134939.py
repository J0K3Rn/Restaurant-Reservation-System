from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
   return render(request, 'accounts/dashboard.htm')

def products (request):
   return HttpResponse('products')

def customer (request):
   return HttpResponse('customer')