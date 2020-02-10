from django.http import HttpResponse
from django.shortcuts import redirect

# Make pages view by admin only


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('food:index')

    return wrapper_func

# Make pages view by user only


def user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('account:home')

    return wrapper_func
