from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.contrib.auth.models import User
from user.models import Profile
from .models import Block,Link
from .design import Theme

from .forms import AvatarForm

from .features import RedirectLink

from datetime import datetime, timedelta

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ssilo4ka(request,username):
    c={}
    user=get_object_or_404(User,username=username)
    profile=user.profile
    c['profile']=profile
    c['profile']=profile
    if profile.priority_link:
        return redirect(profile.priority_link.priority.url)

    return render(request,'ssilo4ka.html',c)

# Links
@login_required
def home(request):
    
    profile=Profile.objects.get(user=request.user)

    c={}
    c['profile']=profile
    
    blocks=profile.block.all()
    blocks_delete=blocks.filter(to_delete=True)
    if len(blocks_delete)>0:
        for block in range(len(blocks)):
            block.delete()
    c['blocks']=blocks.filter(to_delete=False)

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
    return HttpResponse("K")

def update_title(request):
    block=Block.objects.get(uid=request.POST.get('uid'))
    block.link.title=request.POST.get('title')
    block.link.save()
    return HttpResponse("K")

def update_url(request):
    block=Block.objects.get(uid=request.POST.get('uid'))
    block.url=request.POST.get('url')
    block.save()
    return HttpResponse("K")

# json Features

## Redirect feature

def create_redirect_link(request):

    profile=Profile.objects.get(user=request.user)
    
    block_uid=request.POST.get('uid')
    block=Block.objects.get(uid=block_uid)
    
    if profile.redirect_link:
        #profile.redirect_link.delete()
        pass
    time=datetime.today()
    tomorrow=time+timedelta(hours=24)

    end_date=datetime.strftime(tomorrow,'%Y-%m-%d')
    end_time=datetime.strftime(tomorrow,'%H:%M')

    redirect_link=RedirectLink.objects.create(end_date=end_date,end_time=end_time,timezone='+3')
    block.redirect=redirect_link
    block.save()

    profile.redirect_link=block
    profile.save()

    return HttpResponse('K')

def delete_redirect_link(request):



    return render(JsonResponse({"response":"OK",}))

def update_redirect_link_date(request):



    return render(JsonResponse({"response":"OK",}))

def redirect_update_time(request):

    profile=Profile.objects.get(user=request.user)
    redirect_object=profile.redirect_link.redirect

    new_time=request.POST.get('time')
    timezone=redirect_object.timezone

    if timezone!='+3':

        timezone_operator=timezone[0]
        timezone_digit=int(timezone[1])

        time=new_time.split(':')
        hours=time[0]
        minutes=int(time[1])

        if len(hours)==2 and hours[0]=='0':
            hours=int(hours[1])
        else:
            hours=int(hours)

        if timezone_operator=='-':
            hours=hours-timezone_digit-3
            if hours<0:
                hours=24+hours # calculate new hours
                # subtract 1 from date
                #redirect_object.date=
                new_time=f"{hours}:{minutes}" # see if it needs a 0
        else: # (+3)
            if timezone_digit>3:
                to_add=timezone_digit-3
                hours=hours+to_add
            else:
                to_subtract=3-timezone_digit
                hours=hours-to_subtract
    if int(hours)>24:
        hours=hours-24
        # add 1 day to date
    elif int(hours)<24:
        hours=abs(hours)
        # subtract 1 day from date

    new_time=f"{hours}:{minutes}"
    print(new_time)

    redirect_object.end_time=new_time
    redirect_object.save()

    # Testing
    print(new_time)
    print(redirect_object.end_time)

    return HttpResponse('K')

def update_redirect_link_timezone(request):



    return render(JsonResponse({"response":"OK",}))

# htmx

def add_link(request):
    rp=request.POST
    profile=Profile.objects.get(user=request.user)
    block=Block.objects.create(url='')
    link=Link.objects.create(title='',block=block)
    block.link=link
    block.save()
    profile.block.add(block)

    return render(request,'app/links/blocks.html',{'blocks':profile.block.all()})

def delete_block(request):

    block=Block.objects.get(uid=request.POST.get('uid'))
    block.to_delete=True
    block.save()


    return HttpResponse('K')

def undo_block_delete(request):

    block=Block.objects.get(uid=request.POST.get('uid'))
    block.to_delete=False
    block.save()

    return HttpResponse('K')

def delete_all(request):
    profile=Profile.objects.get(user=request.user)
    blocks=profile.block.all().delete()
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