from django.contrib.auth.models import User
from LoginSystemApp.models import UserInfo
from django import forms
from django.forms import TextInput,ModelForm,EmailInput,PasswordInput

class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
        widgets ={
            'first_name':TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username':TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password':PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserInfo
        fields = ('profile_pic',)
        



