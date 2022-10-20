from django.urls import path,include
from .views import *
from django.contrib.auth import logout

app_name='user'

urlpatterns=[
    path('check-username/',check_username,name='check-username'),
    path('register/profile-creation/',profile_creation,name='profile-creation'),
    path('register/<str:username>/',landing_register,name='landing-register'),
    path('register/',register,name='register'),
    path('login/',log_in,name='login'),
    path('password-reset/',password_reset,name='password-reset'),
    path('logout/',logout,name='logout'),
    
    path('',include('app.urls')),
]