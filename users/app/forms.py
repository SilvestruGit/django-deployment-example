from django import forms
from django.contrib.auth.models import User
from app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=32)

    class Meta():
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username':'Max length 150 characters',
            'email':'',
            'password':'Siuuuu',
        }

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

