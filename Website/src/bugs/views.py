from django.shortcuts import render

from .forms import BugForm

from .models import Bug

# Create your views here.

def bug_create_view(request):
	my_form = BugForm()
	if request.method == "POST":
		my_form = BugForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Bug.objects.create(my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		"form": my_form
	}
	return render(request, "bugs/bug_create.html", context)
