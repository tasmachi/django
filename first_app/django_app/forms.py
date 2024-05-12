from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfoForm



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

class UserPortfolioInfo(forms.ModelForm):
    class Meta:
        model=UserProfileInfoForm
        fields=('portfolio_site','portfolio_pic')



    