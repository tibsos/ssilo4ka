from django.shortcuts import render


def landing_register(request,username):

    c={}
    c['username']=username

    return render(request,'templates/auth/register.html',c)