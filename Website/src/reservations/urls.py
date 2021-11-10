from django.urls import path
from . import views


urlpatterns = [
     path('Homepage', views.Homepage, name="Homepage"),
     path("guest_res", views.guest_res, name="guest_res")
]