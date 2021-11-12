from django.db import models

# Create your models here.
class Member(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.EmailField()
	bill_address = models.TextField()
	points = models.IntegerField()
	pref_payment = models.TextField()

class New_Member(models.Model):
	first_name = models.TextField(verbose_name="first_name", null=False, max_length=30, unique=False)
	last_name = models.TextField(verbose_name="last_name", null=False, max_length=30, unique=False)
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	password1 = models.TextField()
	password2 = models.TextField()
	DateCreated = models.DateTimeField(auto_now_add=True)