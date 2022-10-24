from django.urls import path,include
from django.conf import settings

from .views import *
from django.contrib.auth.views import LogoutView

app_name='user'

urlpatterns=[
    path('check-username/',check_username,name='check-username'),
    path('register/profile-creation/',profile_creation,name='profile-creation'),
    path('register/<str:username>/',landing_register,name='landing-register'),
    path('register/',register,name='register'),
    path('login/',log_in,name='login'),
    path('password-reset/',password_reset,name='password-reset'),
    path('logout/',LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    
    path('',include('app.urls')),
]