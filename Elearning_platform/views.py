from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.template import TemplateDoesNotExist
from django.utils.decorators import method_decorator
from django.views import View

from .decoraters import authenticate_user, login_required
from .forms import CreateUser, EditUserProfile


# creating view for home page
class Home(View):
    # handling get requests
    def get(self, request):
        try:
            return render(request, 'home.html')
        except TemplateDoesNotExist:
            return HttpResponse("page not found")

    def post(self, request):
        try:
            return render(request, 'home.html')
        except TemplateDoesNotExist:
            return HttpResponse("page not found")


# creating view for Signup page
class Signup(View):
    # handling get requests

    @method_decorator(authenticate_user)
    def get(self, request):
        try:
            form = CreateUser()
            return render(request, 'signup.html', {'form': form})

        except TemplateDoesNotExist:
            return HttpResponse("Page not found")

    # handling post requests
    def post(self, request):

        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponse(f"{form.errors}")


# creating view for login page
class Login(View):
    # handling get requests
    @method_decorator(authenticate_user)
    def get(self, request):
        try:
            return render(request, 'login.html')
        except TemplateDoesNotExist:
            return HttpResponse("Page not found")

    # handling post requests
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/')
        else:
            return HttpResponse('Username or password Incorrect')


# Creating Edit profile view
class User_profile(View):

    @method_decorator(login_required)
    def get(self, request):
        uid = request.user
        edit_profile = EditUserProfile(instance=uid)
        return render(request, 'profile.html', {'profile_formset': edit_profile})

    @method_decorator(login_required)
    def post(self, request):
        uid = request.user
        edit_profile_form = EditUserProfile(request.POST, instance=uid)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('/login/')
        return render(request, '/profile/')


# Creating view for logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


# Creating view for user Creation
class Inherited_user(View):
    def get(self, request):
        form = CreateUser()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': form})
        else:
            return HttpResponse('Error')
