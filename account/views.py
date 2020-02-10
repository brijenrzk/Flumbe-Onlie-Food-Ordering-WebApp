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


@login_required(login_url='account:login')
@admin_only
def home(request):
    f = Food.objects.all()
    o = Order.objects.all()
    c = Customer.objects.all()
    cat = Category.objects.all()
    total_food = f.count()
    total_order = o.count()
    total_customer = c.count()
    total_category = cat.count()
    return render(request, 'account/dashboard.html', {"total_food": total_food, "total_order": total_order, "total_customer": total_customer, "total_category": total_category})


@login_required(login_url='account:login')
@admin_only
def category(request):
    return render(request, "account/category.html", {"cat": Category.objects.all()})


@login_required(login_url='account:login')
@admin_only
def delete_category(request, pk=None):
    cat = Category.objects.get(pk=pk)
    cat.delete()
    return redirect('account:category')


@login_required(login_url='account:login')
@admin_only
def update_category(request, pk=None):
    cat = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(data=request.POST, initial={'name': cat.name})
        if form.is_valid():
            n = form.cleaned_data.get('name')
            check = Category.objects.filter(name__iexact=n).exists()
            if check:
                return render(request, "account/update-category.html", {"form": form, 'error': "Category already exists"})
            else:
                cat.name = n
                cat.save()
                return redirect('account:category')
    else:
        form = CategoryForm(initial={'name': cat.name})
        return render(request, "account/update-category.html", {"form": form})


@login_required(login_url='account:login')
@admin_only
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            n = form.cleaned_data.get('name')
            check = Category.objects.filter(name__iexact=n).exists()
            if check:
                return render(request, "account/add-category.html", {"form": form, 'error': "Category already exists"})
            else:
                form.save()
                return redirect('account:category')
    else:
        form = CategoryForm()
        return render(request, "account/add-category.html", {"form": form})


@login_required(login_url='account:login')
@admin_only
def food(request):
    return render(request, "account/foods.html", {"food": Food.objects.all()})


@login_required(login_url='account:login')
@admin_only
def delete_food(request, pk=None):
    f = Food.objects.get(pk=pk)
    f.delete()
    return redirect('account:food')


@login_required(login_url='account:login')
@admin_only
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            f = Food()
            f.name = form.cleaned_data.get('name')
            f.price = form.cleaned_data.get('price')
            f.description = form.cleaned_data.get('description')
            f.cat_id_id = form.cleaned_data.get('category')
            f.photo = form.cleaned_data.get('photo')
            f.save()
            return redirect('account:food')
    else:
        form = FoodForm()
        return render(request, "account/add-food.html", {"form": form})


@login_required(login_url='account:login')
@admin_only
def update_food(request, pk=None):
    f = Food.objects.get(id=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, initial={
                        'name': f.name, 'price': f.price, 'description': f.description, 'category': f.cat_id_id, 'photo': f.photo})
        if form.is_valid():
            f.name = form.cleaned_data.get('name')
            f.price = form.cleaned_data.get('price')
            f.description = form.cleaned_data.get('description')
            f.cat_id_id = form.cleaned_data.get('category')
            f.photo = form.cleaned_data.get('photo')
            f.save()
            return redirect('account:food')
    else:
        form = FoodForm(initial={'name': f.name, 'price': f.price,
                                 'description': f.description, 'category': f.cat_id_id, 'photo': f.photo})
        return render(request, "account/update-food.html", {"form": form})


@login_required(login_url='account:login')
@admin_only
def all_orders(request):
    return render(request, "account/all-orders.html", {"ord": Order.objects.all()})
