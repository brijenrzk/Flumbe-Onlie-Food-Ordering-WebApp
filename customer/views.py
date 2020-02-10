from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm, UpdateForm2
from django.contrib import messages
from food.forms import OrderForm
from django.conf import settings
from .models import Customer
from food.models import Food, Order, CartItem
from account.decorators import user_only

# Create your views here.


@login_required(login_url='account:login')
@user_only
def edit_profile(request):  # Edit Profile Method
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=request.user, initial={
                          'address': request.user.customer.address, 'contact': request.user.customer.contact, 'photo': request.user.customer.photo})
        userForm = UpdateForm2(request.POST, instance=request.user, initial={'username': request.user.username, 'first_name': request.user.first_name,
                                                                             'last_name': request.user.last_name, 'email': request.user.email})
        if form.is_valid() and userForm.is_valid():
            c = Customer.objects.get(
                user_id=request.user.id)
            c.address = form.cleaned_data['address']
            c.contact = form.cleaned_data['contact']
            c.photo = form.cleaned_data['photo']
            c.save()
            u = User.objects.get(id=request.user.id)
            u.username = userForm.cleaned_data['username']
            u.first_name = userForm.cleaned_data['first_name']
            u.last_name = userForm.cleaned_data['last_name']
            u.email = userForm.cleaned_data['email']
            u.save()
            return redirect('customer:profile')
    else:
        userForm = UpdateForm2(instance=request.user, initial={'username': request.user.username, 'first_name': request.user.first_name,
                                                               'last_name': request.user.last_name, 'email': request.user.email})
        form = UpdateForm(instance=request.user, initial={
            'address': request.user.customer.address, 'contact': request.user.customer.contact, 'photo': request.user.customer.photo})
    args = {'form': form, 'userForm': userForm}
    return render(request, 'customer/edit-profile.html', args)


@login_required(login_url='account:login')
@user_only
def profile(request):  # Display User Profile method
    return render(request, 'customer/profile.html', {"usr": User.objects.get(pk=request.user.id)})


@login_required(login_url='account:login')
@user_only
def order(request, pk=None):  # Add To Cart method
    if request.method == 'POST':
        formOrder = OrderForm(data=request.POST, initial={'quantity': 1})
        if formOrder.is_valid():
            u = Customer.objects.get(user_id=request.user.id)
            q = formOrder.cleaned_data['quantity']
            c = CartItem(cus_id_id=u.id)
            c.food_id_id = pk
            c.quantity = q
            c.save()
        messages.success(request, 'Added to cart.')
    return redirect(reverse('food:index'))


@login_required(login_url='account:login')
@user_only
def list_order(request):  # list all the current user Order method
    u = Customer.objects.get(user_id=request.user.id)
    o = CartItem.objects.filter(cus_id_id=u.id)
    total = 0
    for ord in o:
        subTotal = ord.quantity * ord.food_id.price
        total += subTotal
    msg = False
    if request.method == 'POST':
        c = CartItem.objects.filter(cus_id_id=u.id)
        for item in c:
            orde = Order(cus_id_id=u.id)
            orde.food_id_id = item.food_id_id
            orde.quantity = item.quantity
            orde.save()
            print(orde.date_order)
        print(Order.objects.all().count())
        msg = True
        c.delete()

    return render(request, 'customer/orders.html', {"ord": CartItem.objects.filter(cus_id_id=u.id), "total": total, "msg": msg})


@login_required(login_url='account:login')
@user_only
def delete_food(request, pk=None):  # Delete food from Cart method
    c = CartItem(id=pk)
    c.delete()
    return redirect(reverse('customer:list_order'))


@login_required(login_url='account:login')
@user_only
def order_history(request):  # Display and download Order History method
    u = Customer.objects.get(user_id=request.user.id)
    f = open("static/order/order-history.txt", "w+")
    orde = Order.objects.filter(cus_id_id=u.id)
    for o in orde:
        subtotal = o.quantity * o.food_id.price
        f.write("Food : "+o.food_id.name+"\n")
        f.write("Price : "+str(o.food_id.price)+"\n")
        f.write("Quantity : "+str(o.quantity)+"\n")
        f.write("Sub Total :"+str(subtotal)+"\n")
        f.write("Date : "+str(o.date_order)+"\n")
        f.write("---------------------------------------\n")
    f.close()

    return render(request, 'customer/order-history.html', {"ord": orde})
