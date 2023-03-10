from urllib import request
from django.urls import path
from Elearning_platform.views import Home, Login, Signup, Logout, User_profile

# CreateUser
app_name = 'Elearning_platform'
urlpatterns = [
        path('', Home.as_view(), name='/'),
        path('login/', Login.as_view(), name='login'),
        path('signup/', Signup.as_view(), name='signup'),
        path('logout/', Logout.as_view(), name='logout'),
        path('profile/', User_profile.as_view(), name='profile'),
]
