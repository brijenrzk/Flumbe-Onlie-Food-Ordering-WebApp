from django.shortcuts import render, redirect
from .models import Food, Customer
from django.db.models import Q
from .forms import OrderForm
from account.decorators import user_only
# Create your views here.

def all_foods(request):
    OrderF = OrderForm(initial={'quantity':1})
    return render(request=request, template_name="food/all-food.html", context={"food": Food.objects.all(), "orderForm": OrderF})


@user_only
def index(request):
    OrderF = OrderForm(initial={'quantity':1})

    return render(request=request, template_name="food/index.html", context={"food": Food.objects.all(), "orderForm": OrderF})


def list_foods(request):
    query = ""
    context = {}
    if request.GET:
        query = request.GET['q']
    food = get_data_queryset(query)
    context['food'] = food
    return render(request, "food/search-result.html", context)


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        foods = Food.objects.filter(
            Q(name__icontains=q) | Q(price__icontains=q)
        )

        for food in foods:
            queryset.append(food)

    return (set(queryset))
