from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "api"
urlpatterns = [
    path('api/', views.api_data, name="api_data"),
    path('api/<int:pk>', views.api_edit_data, name="api_edit_data"),
    path('api/page/<int:PAGENO>', views.api_food_pagination,
         name="api_food_pagination"),
]
