from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class BoxForm(ModelForm):

    def clean(self):
        cleaned_data = super(BoxForm, self).clean()
        city = cleaned_data.get("city")
        state = cleaned_data.get("state")

        if not city == "Singapore":
            raise forms.ValidationError("City must be 'Singapore'")
        if not state == "Singapore":
            raise forms.ValidationError("State must be Singapore")
        return(cleaned_data)

    class Meta:
        model = RequestDonationBox
        fields = ['name', 'email', 'phone', 'state', 'city', 'address', 'sub_group']
