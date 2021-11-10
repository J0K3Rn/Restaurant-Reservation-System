from django.shortcuts import render

from .forms import MemberForm

from .models import Member

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login (request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password =password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'invaild credentials')
			return redirect('login')
			
	else:
		return render(request, 'register.html')

def member_create_view(request):
	my_form = MemberForm()
	if request.method == "POST":
		my_form = MemberForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Member.objects.create(my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		"form": my_form
	}
	return render(request, "members/member_create.html", context)

#def member_login_view(request):
#	my_form

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request, 'Email is Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                return redirect('login')
        else:
            print('password not matching..')
        return redirect('/')
    else:
        print('password not matching..')
    return render(request, 'register.html')

def login_reserve(request):
    return(render(request, 'login_reserve.html'))

def login(request):
    return(render(request, 'login.html'))

def register(request):
	return(render(request, 'register.html'))

def login_reserve(request):
	return(render(request, 'login_reserve.html'))

def login(request):
	return(render(request, 'login.html'))