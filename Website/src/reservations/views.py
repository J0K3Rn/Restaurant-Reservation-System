from django.shortcuts import render

from .forms import ReservationForm

from .models import Reservation

# Create your views here.

def reservation_create_view(request):
	my_form = ReservationForm()
	if request.method == "POST":
		my_form = ReservationForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Reservation.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		"form": my_form
	}
	return render(request, "reservations/reservation_create.html", context)

def Homepage(request):
	return render(request, "home1.html")

def guest_reserve(request):
	return render(request, "login_reserve.html")