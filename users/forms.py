from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",
                "username",
                "email",
                "password1",
                "password2",
                "phone",
                "role"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))