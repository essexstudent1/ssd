# This is a new file created for the SSD forms
# This code is partially adapted from https://www.youtube.com/watch?v=eCeRC7E8Z7Y

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from report.models import PublicUser,Report

# This section defines the form to register a new user

class UserRegistrationForm(UserCreationForm):

  email = forms.EmailField(required=True)
  
  class Meta:
        model = PublicUser
        fields = ('email', 'password1', 'password2', 'firstName', 'lastName', 'address', 'town', 'province', 'country', 'postcode', 'security_question', 'security_answer')


# This section defines the form to log in a user

class UserAuthenticationForm(forms.ModelForm):

  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
    model = PublicUser
    fields = ('email', 'password')

  def clean(self):
    if self.is_valid():
      email = self.cleaned_data['email']
      password = self.cleaned_data['password']
      if not authenticate(email=email, password=password):
        raise forms.ValidationError("Invalid login")


# This section defines the form to require 2FA authentication

class UserMFAAuthenticationForm(forms.ModelForm):

  class Meta:
    model = PublicUser
    fields = ('security_answer',)

#This section defines the form for report breach
class ReportForm(forms.ModelForm):
  class Meta:
    model = Report
    fields = ('person_id', 'data_breach_details','responsible_party','others_notified','data_breach_noticed_on',)
    widgets = {
            'person_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_breach_details': forms.TextInput(attrs={'class': 'form-control'}),
            'responsible_party': forms.TextInput(attrs={'class': 'form-control','id':'exampleFormControlTextarea1'}),
            'others_notified': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_breach_noticed_on':forms.DateInput(attrs={'class': 'form-control'}),
            

           
        }
    

  
