from django.urls import path
from . import views


urlpatterns = [
    # path('register', views.register, name="register"),
    path('login_reserve', views.login_reserve, name='login_reserve'),
    # path('login',views.login, name='login'),
    path('signup/', views.signup, name="signup") ,
    path('login/', views.login, name="login") , 
    path('handlesignup/', views.handlesignup, name="handlesignup"),
    path('handlelogin/', views.handlelogin, name="handlelogin"),
    path('handlelogout/', views.handlelogout, name="handlelogout")

]