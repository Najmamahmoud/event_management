# events/forms.py

from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateField(widget=forms.SelectDateWidget)
    location = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
