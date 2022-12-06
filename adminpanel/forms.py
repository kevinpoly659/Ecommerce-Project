from django import forms
from products.models import products

class Imageform(forms.ModelForm):
    class Meta:
        model = products
        fields = ('image','image2','image3','image4')
        
