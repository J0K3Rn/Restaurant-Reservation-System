from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField("Customer Name", default="John Doe",max_length=120)
    email_address = models.EmailField("Email Address", blank=True)
    phone = models.CharField("Contact Phone", max_length =20, blank=True)
    Lagos = "LAGOS"
    Abuja = "ABUJA"
    LOCATIONS = [
        (Lagos, 'LAGOS'),
        (Abuja, "ABUJA")]

    location = models.CharField(
        max_length=200, choices=LOCATIONS, blank=True
    )

class reservation (models.Model):
    name = models.CharField('Customer Name', max_length=120, blank=False)
    datetime= models.DateTimeField()
    time = models.CharField("Reservation time", max_length=10, blank=True)
    partysize = models.IntegerField()


