from django.urls import path
from .views import *
urlpatterns=[
    path('',landing,name='landing'),
    path('<slug:categorySlug>/',category,name='category'),
    path('<slug:postSlug>/',post,name='article'),
]