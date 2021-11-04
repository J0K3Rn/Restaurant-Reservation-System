from django import forms

from .models import Reservation

class ReservationForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone_num = forms.CharField()
	email = forms.EmailField()
	date_time = forms.DateTimeField()
	num_guests = forms.IntegerField()
