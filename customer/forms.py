from django import forms

from .models import Customer
from django.contrib.auth.models import User


class UpdateForm(forms.ModelForm):  # Update form for Customer Model
    class Meta:
        model = Customer
        fields = ('address', 'contact', 'photo')


class UpdateForm2(forms.ModelForm):  # Update form for User Model

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')
