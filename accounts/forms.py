from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class EmpSignupForm(forms.Form):
#     Name = forms.CharField(max_length=100,required=True)
#     Email = forms.EmailField(max_length=100,required=True)
#     username = forms.CharField(max_length=100,required=True)
#     password1 = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)

class EmpSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    # isemployee = forms.BooleanField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","is_staff"]

class EmpLoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)
