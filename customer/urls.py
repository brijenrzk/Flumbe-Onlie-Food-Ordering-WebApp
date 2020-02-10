from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "customer"
urlpatterns = [
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('profile/', views.profile, name="profile"),
    path('food/order/', views.list_order, name="list_order"),
    path('food/order/<int:pk>/', views.order, name="order"),
    path('food/order/delete/<int:pk>/', views.delete_food, name="delete_food"),
    path('profile/order-history/', views.order_history, name="order_history"),
]
