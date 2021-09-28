from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
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

def createOrder(request):

   form = OrderForm()
   if request.method =="POST":
      form = OrderForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/')
   context = {'form':form}
   return render(request, 'accounts/order_form.htm', context)

def updateOrder(request, pk):
   order = Order.object.get(id=pk)
   form  = OrderForm(instance=order)
   context = {'form':form}
   return render(request, 'accounts/order_form.htm', context)

def register(request):
   return render(request, 'accounts/register.htm')

def login (request):
   return render(request, 'accounts/login.htm')

def qualification (request):
   return render(request, 'accounts/qualification.htm')