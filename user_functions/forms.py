from django import forms
from .models import *
from django.forms import TextInput
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    userName = forms.CharField(required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
    class Meta: 
        model = User
        exclude = ('UserEmail', 'UserLevel', 'UserDate', 'UserStatus', 'UserPerson')


class CreateUserForm(forms.ModelForm):
    username = forms.CharField(label='User Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%; font-family: Arial;', 'class': 'form-control'}))
    password = forms.CharField(label='Password', required = True, widget=forms.PasswordInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    passwordConfirm = forms.CharField(label='Confirm Password', required = True, widget=forms.PasswordInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    email = forms.CharField(label='Email', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'password', 'passwordConfirm', 'email')
        
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()

class CreatePersonForm(forms.ModelForm):
    FirstName = forms.CharField(label='First Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    LastName = forms.CharField(label='Last Name', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Phone = forms.CharField(label='Phone Number', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Affiliation = forms.CharField(label='Organization', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    Address = forms.CharField(label='Address', required = True, widget=forms.TextInput(attrs={'style': 'width: 100%;', 'class': 'form-control'}))
    
    class Meta:
        model = Person
        fields = ('FirstName', 'LastName', 'Phone', 'Affiliation', 'Address')
    