# forms.py
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
   class Meta:
      model = Order
      field = '__all__'