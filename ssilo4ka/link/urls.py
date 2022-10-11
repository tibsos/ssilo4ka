from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home,name='home')
]

htmx_urlpatterns=[
    path('add-link/',add_link,name='add-link'),
]
urlpatterns+=htmx_urlpatterns