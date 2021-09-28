from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.



#____________________________________________________________________________
def home(request):
   orders = Order.objects.all()
   customers = Customer.objects.all()

   total_customers = customers.count()

   total_orders =orders.count()
   delivered = orders.filter(status='Delivered').count()
   pending = orders.filter(status='Pending').count()

   context = {'orders':orders, 'customers':customers,
   'total_orders':total_orders, 'delivered':delivered,
   'pending':pending}

   return render(request, 'accounts/dashboard.htm', context) #renders both the page its content from the view. 

def products(request):
   products = Product.objects.all()
   return render(request, 'accounts/products.htm', {'products': products})

def customer(request, pk_test):
   customer = Customer.objects.get(id=pk_test)

   orders = customer.order_set.all()
   order_count = orders.count()

   context = {'customer':customer, 'orders':orders, 'order_count':order_count}
   return render(request, 'accounts/customer.htm', context)

def register(request):
   return render(request, 'accounts/register.htm')

def login (request):
   return render(request, 'accounts/login.htm')