from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "account"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.customerLogin, name="login"),
    path('logout/', views.customerLogout, name="logout"),
    path('dashboard/', views.home, name="home"),
    path('dashboard/category', views.category, name="category"),
    path('dashboard/add-category', views.add_category, name="add_category"),
    path('dashboard/category/delete/<int:pk>/',
         views.delete_category, name="delete_category"),
    path('dashboard/category/update/<int:pk>/',
         views.update_category, name="update_category"),
    path('dashboard/food', views.food, name="food"),
    path('dashboard/food/delete/<int:pk>/',
         views.delete_food, name="delete_food"),
    path('dashboard/add-food', views.add_food, name="add_food"),
    path('dashboard/food/update/<int:pk>/',
         views.update_food, name="update_food"),
    path('dashboard/all-orders', views.all_orders, name="all_orders"),
]
