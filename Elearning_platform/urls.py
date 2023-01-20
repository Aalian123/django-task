from django.urls import path
from Elearning_platform.views import CreateUser, Home, Login, Signup

app_name = 'Elearning_platform'
urlpatterns = [
        path('', Home.as_view()),
        path('signup/', Signup.as_view()),
        path('login/', Login.as_view()),
        path('adduser/', CreateUser.as_view(), name='create-user')
]
