from django import forms

from .models import Member

class MemberForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	bill_address = forms.CharField()
	points = forms.IntegerField()
	pref_payment = forms.CharField()
