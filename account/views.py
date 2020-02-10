from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegisterForm, ProfileForm, CategoryForm, FoodForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from food.models import Customer, Food, Category, Order, Customer
from .decorators import admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        formRegister = RegisterForm(data=request.POST)
        formProfile = ProfileForm(
            data=request.POST)
        if formRegister.is_valid() and formProfile.is_valid():
            user = formRegister.save()
            user.set_password(user.password)
            user.save()
            #us = User.objects.get(pk=user.id)
            #customer = Customer()
            profile = formProfile.save(commit=False)
            profile.user = User.objects.get(pk=user.id)
            #customer.user_id = us
            # print(user.id)
            profile.save()
            username = formRegister.cleaned_data.get('username')
            password = formRegister.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('customer:profile')
        else:

            return render(request, "account/register.html", {'error': "Given Username is Already Taken.Please Try Another."})

    else:
        formRegister = RegisterForm()
        formProfile = ProfileForm()
        return render(request, "account/register.html", {"formRegister": formRegister, "formProfile": formProfile})


def customerLogin(request):
    if request.method == 'POST':
        usernam = request.POST['username']
        passwor = request.POST['password']
        user = auth.authenticate(request, username=usernam, password=passwor)
        if user is not None:
            auth.login(request, user)
            return redirect('account:home')

        else:
            return render(request, "account/login.html", {'error': "Worng Username and Password"})
    else:
        return render(request, "account/login.html")


def customerLogout(request):
    logout(request)
    return redirect('account:home')


