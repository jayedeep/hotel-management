from django import forms
from .models import Restaurants,Foods,Invoice
from django.contrib.auth.models import User

class CreateUser(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password','password2']

class LoginUser(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class RestaurantsForm(forms.ModelForm):
    class Meta:
        model=Restaurants
        fields=['name','city','address','franchise']

class FoodsForm(forms.ModelForm):
    class Meta:
        model=Foods
        fields=['restaurant','name','price','created_at']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['restaurants','table_no','foods','datetime','totalbill']

