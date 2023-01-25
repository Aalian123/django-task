from django.urls import path
from Elearning_platform.views import Home, Login, Signup, Inherited_user, Logout

# CreateUser
app_name = 'Elearning_platform'
urlpatterns = [
        path('', Home.as_view(), name='/'),
        path('signup/', Signup.as_view(), name='signup'),
        path('login/', Login.as_view(), name='login'),
        path('logout/', Logout.as_view(), name='logout'),
        path('inherit/', Inherited_user.as_view(), name='inherit')
        # path('adduser/', CreateUser.as_view(), name='create-user')
]
