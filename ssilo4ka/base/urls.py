from django.urls import path,include
from .views import *

app_name='base'

urlpatterns=[
    path('',landing,name='landing'),
]