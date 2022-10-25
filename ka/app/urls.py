from django.urls import path,include
from .views import *

app_name='app'

urlpatterns=[
    path('',home,name='home'),
]