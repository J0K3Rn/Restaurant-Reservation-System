from django.db import models

# Create your models here.
class Member(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	email = models.EmailField()
	password = models.TextField()
	bill_address = models.TextField()
	points = models.IntegerField()
	pref_payment = models.TextField()
