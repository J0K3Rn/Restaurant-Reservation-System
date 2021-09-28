from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/', views.products),
    path('customer/', views.customer),
    path('register/', views.register),


]