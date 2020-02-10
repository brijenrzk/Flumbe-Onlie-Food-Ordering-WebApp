from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "food"
urlpatterns = [
    path('', views.index, name="index"),
    path('food/', views.list_foods, name="list_foods"),
    path('all-food/', views.all_foods, name="all_foods"),
]
