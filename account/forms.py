from django import forms
from django.contrib.auth.models import User
from food.models import Customer, Category, Food


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('address', 'contact')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class FoodForm(forms.Form):
    name = forms.CharField(max_length=35)
    price = forms.IntegerField()
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea()
    )
    category = forms.ChoiceField(
        choices=[(cat.id, cat.name) for cat in Category.objects.all()])

    photo = forms.ImageField()

    def clean(self):
        cleaned_data = super(FoodForm, self).clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        category = cleaned_data.get('category')
        photo = cleaned_data.get('photo')
