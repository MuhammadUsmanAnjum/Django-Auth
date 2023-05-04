# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']
        
        

