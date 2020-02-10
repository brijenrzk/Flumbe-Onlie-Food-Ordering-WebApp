from django import forms

from .models import Customer
from django.contrib.auth.models import User


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'contact', 'photo')


class UpdateForm2(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')
