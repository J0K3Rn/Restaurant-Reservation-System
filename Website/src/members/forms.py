from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member

class MemberForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	bill_address = forms.CharField()
	points = forms.IntegerField()
	pref_payment = forms.CharField()


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user