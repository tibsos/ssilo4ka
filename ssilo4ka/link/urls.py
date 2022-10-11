from django.urls import path
from .views import *

app_name='link'

urlpatterns=[
    path('home/',home,name='home')
]

htmx_urlpatterns=[
    path('add-link/',add_link,name='add-link'),
]
urlpatterns+=htmx_urlpatterns