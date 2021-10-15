from django.db import models

# Create your models here.
class Reservation(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()
	phone_num = models.TextField()
	email = models.EmailField()
	date_time = models.DateTimeField()
	num_guests = models.PositiveSmallIntegerField
