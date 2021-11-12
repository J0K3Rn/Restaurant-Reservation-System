from django.urls import path
from . import views


urlpatterns = [
     path('Homepage', views.Homepage, name="Homepage"),
     path("guest_reserve", views.guest_reserve, name="guest_reserve")
]