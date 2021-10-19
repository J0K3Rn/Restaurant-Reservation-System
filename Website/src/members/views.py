from django.shortcuts import render

from .forms import MemberForm

from .models import Member

# Create your views here.

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
