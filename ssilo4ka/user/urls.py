from django.urls import path,include
from .views import *

app_name='user'

urlpatterns=[
    path('check-username/',check_username,name='check-username'),
    path('register/profile-creation/',profile_creation,name='profile-creation'),
    path('register/<str:username>/',landing_register,name='landing-register'),
    path('',include('link.urls')),
]