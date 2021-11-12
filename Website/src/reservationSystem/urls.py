"""reservationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import *
from reservations.views import *
#from members.views import member_create_view

urlpatterns = [
    path('', Homepage),
    path('admin/', admin.site.urls),
    path('create/', reservation_create_view),
    #path('accounts/', member_create_view, name='create_account'),
    path('', include('members.urls')),
    path('reservations/', include('reservations.urls')),
    path('pages/', include('pages.urls'))
    
]
