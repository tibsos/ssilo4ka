from django.urls import path,include
from .views import *

app_name='user'

urlpatterns=[
    path('register/<str:username>/',landing_register,name='landing-register'),
    #path('register/',register,name='register'),
]