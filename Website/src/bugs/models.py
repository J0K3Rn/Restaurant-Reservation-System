from django.db import models

# Create your models here.
class Bug(models.Model):
	bug_id = models.IntegerField() # System Generated
	bug_name = models.TextField() # Assigned by developer
	customer_bug_description = models.TextField() # Written by user

