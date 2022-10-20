from django.urls import path
from .views import *
app_name='b'
urlpatterns=[
    path('',l,name='l'),
    path('<slug:s>/',c,name='c'),
    path('<slug:s>/',p,name='a'),
]