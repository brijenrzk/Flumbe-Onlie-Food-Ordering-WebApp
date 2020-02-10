from django import forms

from .models import CartItem


class OrderForm(forms.ModelForm):  # Form for Quantity while Ordering
    class Meta:
        model = CartItem
        fields = ('quantity',)
