from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.models import User
from user.models import Profile
from .models import Block,Link
from .design import Theme

from .forms import AvatarForm

def ssilo4ka(request,username):
    c={}
    user=get_object_or_404(User,username=username)
    profile=user.profile
    c['profile']=profile
    return render(request,'ssilo4ka.html',c)

# Links

def home(request):
    c={}
    profile=Profile.objects.get(user=request.user)
    c['profile']=profile
    c['blocks']=profile.block.all()

    return render(request,'app/home.html',c)

# django forms

def delete_avatar(request):
    profile=Profile.objects.get(user=request.user)
    profile.avatar.delete(save=True)
    profile.save()
    #return JsonResponse({"avatar":profile.avatar})
    return redirect('link:design')

# json

def block_activity(request):
    block=Block.objects.get(uid=request.POST.get('uid'))
    if block.active==True:
        block.active=False
        block.save()
    else:
        block.active=True
        block.save()
    return HttpResponse("OK")

def update_title(request):
    block=Block.objects.get(uid=request.POST.get('uid'))
    block.link.title=request.POST.get('title')
    #block.link.save()
    return HttpResponse("OK")

def update_url(request):
    block=Block.objects.get(uid=request.POST.get('uid'))
    block.link.url=request.POST.get('url')
    block.link.save()
    return HttpResponse("OK")

# htmx

def add_link(request):
    rp=request.POST
    profile=Profile.objects.get(user=request.user)
    block=Block.objects.create()
    link=Link.objects.create(title='', url='',block=block)
    block.link=link
    block.save()
    profile.block.add(block)

    return render(request,'app/links/blocks.html',{'blocks':profile.block.all()})

def delete_block(request,uid):
    profile=Profile.objects.get(user=request.user)
    Block.objects.get(uid=uid).delete()
    blocks=profile.block.all()
    return render(request,'app/links/blocks.html',{'blocks':blocks})

def delete_all(request):
    profile=Profile.objects.get(user=request.user)
    profile.block.all().delete()
    return render(request,'app/links/blocks.html',{'blocks':None})


# Design 

def design(request):
    c={}
    profile=Profile.objects.get(user=request.user)
    c['profile']=profile
    c['avatar_form']=AvatarForm()
    c['themes']=Theme.objects.all()
    
    if request.POST.get("form_type") == 'avatar-form':
        form=AvatarForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            profile.avatar=form.cleaned_data['avatar']
            profile.save()
            return JsonResponse({'response':'OK'})
        else:
            formats=[]
            return JsonResponse({'response':'У вашей картинки недопустимый формат :( \n Пожалуйста, загрузите картинку с одним из нижеперечисленных форматом =)','formats':', '.join(formats)})

    return render(request,'app/design/design.html',c)


def analytics(request):
    c={}
    profile=Profile.objects.get(user=request.user)
    c['profile']=profile
    return render(request,'app/analytics.html',c)


def account(request):
    c={}
    profile=Profile.objects.get(user=request.user)
    c['profile']=profile
    return render(request,'app/account.html',c)