from django import forms

from .models import Bug

class BugForm(forms.Form):
	bug_description = forms.CharField()
