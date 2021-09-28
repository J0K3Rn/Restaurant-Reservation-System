from django.urls import path
from . import views

urlpatterns = [

	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),  #using name makes the link dynamic

    path('', views.home, name="Home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer' ),
    path('qualification/', views.qualification, name="info"),
]