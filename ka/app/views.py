from django.shortcuts import render

def home(request):
    c={}
    c['profile']=request.user
    return render(request,'templates/home.html',c)
