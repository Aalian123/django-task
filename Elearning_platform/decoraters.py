from django.shortcuts import redirect


# Decorators

# to authenticate if user is logged in or not
def authenticate_user(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return func(request, *args, **kwargs)

    return wrapper_func


def login_required(func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return func(request, *args, **kwargs)

    return wrapper_func


# to check if superuser or staff
def is_staff_or_superuser(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return redirect('/admin/')
        return func(request, *args, **kwargs)

    return wrapper_func
