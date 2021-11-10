from django.urls import path
from . import views


urlpatterns = [
     path('navbar', views.navbar, name="navbar"),
]