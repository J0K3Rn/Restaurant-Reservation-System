from django.contrib.auth.models import User, auth

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.contrib import messages
import members

# from members.forms import MemberForm


# def home(request):
#     return render(request, "account/home.html")
# view for rendering signup page
def signup(request):
    return render(request, "signup1.html")
# view for rendering login page
def login(request):
    return render(request, "login1.html")
# view for rendering data coming from signup page
def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("/signup")
            except User.DoesNotExist:
                if len(uname) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("/signup")
                if not uname.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("/signup")
        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, " Your account has been successfully created")
        return redirect("/")
    else:
        return HttpResponse('404 - NOT FOUND ')
# view for rendering data from login page
def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        # cheching for valid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, " Successfully logged in")
            return redirect("/")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404 - NOT FOUND ')
# view for rendering logout
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')


# __________________________________________________________________________________________
# Create your views here.
# def signup(request):
#     return render(request, "Signup.html")

# def login (request):
# 	if request.method =='POST':
# 		username = request.POST['username']
# 		password = request.POST['password']

# 		user = auth.authenticate(username = username, password =password)

# 		if user is not None:
# 			auth.login(request, user)
# 			return redirect('/')
# 		else:
# 			messages.info(request, 'invaild credentials')
# 			return redirect('login')
			
# 	else:
# 		return render(request, 'Signup.html')

# def member_create_view(request):
# 	my_form = MemberForm()
# 	if request.method == "POST":
# 		my_form = MemberForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			members.objects.create(my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "members/member_create.html", context)

#def member_login_view(request):
#	my_form

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 print('username taken')
#                 messages.info(request, 'Username Taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 print('email taken')
#                 messages.info(request, 'Email is Taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save();
#                 print('User created')
#                 return redirect('login')
#         else:
#             print('password not matching..')
#         return redirect('/')
#     else:
#         print('password not matching..')
#     return render(request, 'register.html')

def login_reserve(request):
    return(render(request, 'login_reserve.html'))

# def login(request):
#     return(render(request, 'Signup.html'))
