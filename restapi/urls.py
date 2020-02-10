from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "api"
urlpatterns = [
    path('api/', views.api_data, name="api_data"),
    path('api/<int:pk>', views.api_specific_data, name="api_specific_data"),
    path('api/add', views.api_add_data, name="api_add_data"),
    path('api/update/<int:pk>', views.api_update_data, name="api_update_data"),
    path('api/delete/<int:pk>', views.api_delete_data, name="api_delete_data"),
    path('api/page/<int:PAGENO>', views.api_food_pagination,
         name="api_food_pagination"),
]
