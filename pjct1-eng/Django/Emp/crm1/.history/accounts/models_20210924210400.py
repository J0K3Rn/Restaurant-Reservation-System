from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
   user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
   first_name = models.CharField(max_length=200, null=True, blank=True)
   last_name = models.CharField(max_length=200, null=True, blank=True)
   phone = models.CharField(max_length=200, null=True, blank=True)

   def __str__(self):
      return str(self.user)




def create_profile(sender, instance, created, **kwargs):
   if created:
      Profile.objects.create(user=instance)
      print('Profile created!')


post_save.connect(create_profile, sender=User)

def update_profile(sender, instance, created, **kwargs):
   if created == False:
      instance.profile.save()
      print('Profile Updated!')

#__________________________________________________________________________________________
class Customer(models.Model):
   name=models.CharField(max_length=200, null=True)
   phone=models.CharField(max_length=200, null=True)
   email=models.CharField(max_length=200, null=True)
   date_created=models.DateTimeField(auto_now_add=True, null=True)

   def __str__(self):
      return self.name


class Tag(models.Model):
   name=models.CharField(max_length=200, null=True)


   def __str__(self):
      return self.name


class Product(models.Model):
   CATEGORY = (('Indoor', 'Indoor'),
   ('Out Door', 'Out Door'))

   name= models.CharField(max_length=200, null=True)
   price= models.FloatField(max_length=200, null=True)
   category= models.CharField(max_length=200, null=True, choices=CATEGORY)
   description= models.CharField(max_length=200, null=True)
   date_created= models.DateTimeField(auto_now_add=True, null=True)
   tags = models.ManyToManyField(Tag)




class Order(models.Model):
   STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'), 
            ('Delivered', 'Delivered'))

   customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
   products = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
   date_created = models.DateTimeField(auto_now_add=True, null=True)
   status = models.CharField(max_length=200, null=True, choices=STATUS)
  