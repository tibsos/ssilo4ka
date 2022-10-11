from django.urls import path
from .views import *

app_name='user'

urlpatterns=[
    path('register/<str:username>',landing_register,name='landing-register'),
    path('check_username/',check_username,name='check-username'),
    path('profile_creation/',profile_creation,name='profile-creation'),
]