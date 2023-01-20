from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.views import View
from django.template import TemplateDoesNotExist
from django.views.generic.edit import CreateView
from .models import User_info, User_inherit
from .forms import UserForm


# Generic View for the user_info model
class CreateUser(CreateView):
    template_name = 'Elearning_platform/user_info_form.html'
    form_class = UserForm

    # redirecting to url when submitted
    def get_success_url(self):
        return reverse('Elearning_platform:create-user')


# creating view for Signup page
class Signup(View):
    # handling get requests
    def get(self, request):
        try:
            # getting data from User_inherit() function and passing as dict
            info = User_inherit.get_all_users()
            return render(request, 'signup.html', {'info': info})

        except TemplateDoesNotExist:
            return HttpResponse("Page not found")

    # handling post requests
    def post(self, request):
        try:
            # Getting data from frontend Form
            user_data = request.POST
            model = User_info()
            model.first_name = user_data['f_name']
            model.last_name = user_data['l_name']
            model.email = user_data['email']
            model.phone = user_data['phone']
            model.user_id = user_data['id']
            model.save()
            return render(request, 'signup.html')
        except NotImplemented:
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
        return render(request, 'login.html')


# creating view for home page
class Home(View):
    # handling get requests
    def get(self, request):
        try:
            # getting data from User_info() function and passing as dict
            info = User_info.get_all_users()
            return render(request, 'home.html', {'info': info})
        except TemplateDoesNotExist:
            return HttpResponse("page not found")
