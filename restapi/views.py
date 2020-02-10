from django.shortcuts import render
from food.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


def api_data(request):  # Get all Food data
    food = Food.objects.all()
    dict_value = {
        "food": list(food.values("name", "price", "description"))
    }
    return JsonResponse(dict_value)


def api_specific_data(request, pk=None):  # Get specific food data
    food = Food.objects.get(pk=pk)

    return JsonResponse({"name": food.name, "price": food.price, "description": food.description})


@csrf_exempt
def api_add_data(request):  # Add new food data
    f = Food()
    if request.method == "POST":
        decoded_data = request.body.decode('utf-8')
        food_data = json.loads(decoded_data)
        f.name = food_data['name']
        f.price = food_data['price']
        f.description = food_data['description']
        f.save()
        return JsonResponse({"message": "Completed"})

    else:
        return JsonResponse({"name": f.name, "price": f.price, "description": f.description})


@csrf_exempt
def api_update_data(request, pk=None):  # update food data
    food = Food.objects.get(pk=pk)
    if request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        food_data = json.loads(decoded_data)
        food.name = food_data['name']
        food.price = food_data['price']
        food.description = food_data['description']
        food.save()
        return JsonResponse({"message": "Update Completed"})

    else:
        return JsonResponse({"name": food.name, "price": food.price, "description": food.description})


@csrf_exempt
def api_delete_data(request, pk=None):  # delete food data
    food = Food.objects.get(pk=pk)
    if request.method == "DELETE":
        food.delete()
        return JsonResponse({"message": "Delete Completed"})

    else:
        return JsonResponse({"name": food.name, "price": food.price, "description": food.description})


def api_food_pagination(request, PAGENO):  # pagination
    SIZE = 5
    skip = SIZE * (PAGENO-1)
    food = Food.objects.all()[skip:PAGENO*SIZE]
    dict = {
        "foods": list(food.values("name", "price", "description"))
    }
    return JsonResponse(dict)
