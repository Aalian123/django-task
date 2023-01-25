from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.template import TemplateDoesNotExist
from .forms import CreateUser


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
            return HttpResponse('Can not add users')


# creating view for login page
class Login(View):
    # handling get requests
    def get(self, request):
        try:
            return render(request, 'login.html')
        except TemplateDoesNotExist:
            return HttpResponse("Page not found")

    # handling post requests
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Username or password Incorrect')


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
