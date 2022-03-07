from django import forms
from .models import Grocery

class Grocery_Form(forms.ModelForm):

    class Meta():
        model = Grocery
        fields = {'Name','Type','RatePerUnit','Quantity',}
