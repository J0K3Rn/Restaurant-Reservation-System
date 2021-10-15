from django.db import models

# Create your models here.

class Table(models.Model):
	number = models.PositiveIntegerField(unique=True)
	size = models.PositiveIntegerField()
	inUse = models.BooleanField(default=False)
