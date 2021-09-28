from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer' ),

    path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),  #using name makes the link dynamic
    path('qualification/', views.qualification, name="info"),
    path('create_order/', views.createOrder, name="create_order"),
]