from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name="register"),
    path('login_reserve', views.login_reserve, name='login_reserve'),
    path('login',views.login, name='login')

]