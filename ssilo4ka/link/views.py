from django.shortcuts import render
from user.models import Profile
from .models import Block,Link

def home(request):
    c={}
    profile=Profile.objects.get(user=request.user)
    c['profile']=profile
    c['blocks']=profile.block.all()
    return render(request,'app/home.html',c)


# htmx

def add_link(request):
    rp=request.POST
    profile=Profile.objects.get(user=request.user)
    link=Link.objects.create()
    block=Block.objects.create(link=link)
    profile.block.add(block)

    return render(request,'app/partials/blocks.html',{'blocks':profile.block.all()})