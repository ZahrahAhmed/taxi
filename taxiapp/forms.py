from django import forms
from django.contrib.auth.models import User
from taxiapp.models import Restaurant

class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']
        email = forms.CharField(max_length=100, required=True)
        widgets={
        'password': forms.PasswordInput(),
        }
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','phone','address', 'logo']
