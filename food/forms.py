from django import forms

from .models import CartItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity',)
