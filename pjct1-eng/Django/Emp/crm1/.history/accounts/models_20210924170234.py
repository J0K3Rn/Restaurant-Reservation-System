from django.db import models

# Create your models here.
class Customer(models.Model):
   name=models.CharField(max_length=200, null=True)
   phone=models.CharField(max_length=200, null=True)
   email=models.CharField(max_length=200, )
   date_created=models.CharField(auto_now_add=True, null=True)
