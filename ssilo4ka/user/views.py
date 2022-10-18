from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.http import JsonResponse

from django.contrib.auth import login, authenticate,logout

from .models import Profile,Category,Subcategory


def register(request):

    if request.method=='POST':
        rp=request.POST
        password=rp.get('password1')
        _mutable = rp._mutable
        rp._mutable = True
        rp['password2'] = password
        rp._mutable = _mutable

        form=UserCreationForm(rp)

        if form.is_valid():
            user=form.save()
            user.profile.email=rp.get('email')
            user.save()
            user.refresh_from_db()
            user.profile.analytics=a
            user=authenticate(username=rp.get('username'),password=password)
            login(request,user)
            return redirect('user:profile-creation')

    return render(request,'auth/landing_register.html')

def landing_register(request,username):
    c={}
    c['username']=username   

    if request.method=='POST':
        rp=request.POST
        password=rp.get('password1')
        _mutable = rp._mutable
        rp._mutable = True
        rp['password2'] = password
        rp._mutable = _mutable

        form=UserCreationForm(rp)

        if form.is_valid():
            user=form.save()
            user.profile.email=rp.get('email')
            user.save()
            user.refresh_from_db()
            user=authenticate(username=rp.get('username'),password=password)
            login(request,user)
            return redirect('user:profile-creation')

    return render(request,'auth/landing_register.html',c)

def log_in(request):
    if request.user.is_authenticated:
        return redirect('link:landing')
    else:
        if request.method=='POST':
            user=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            login(request,user)
            return redirect('link:home')

        return render(request,'auth/login.html')
        
def password_reset(request):
    return render(request,'auth/password_reset.html')

def check_username(request):

    usernames=User.objects.values_list('username', flat=True)
    username=request.POST.get('username')

    if username in usernames:
        return JsonResponse({'response':f'Ник \"{username}\" уже используется :('}) 
    else:
        return JsonResponse({'response':''})

def profile_creation(request):

    # Account for those who abused the link (return error)

    c={}
    c['user']=request.user
    c['categories']=Category.objects.all()

    profile=Profile.objects.get(user=request.user)

    if request.method=='POST':
        rp=request.POST
        name=rp.get('name')
        category=rp.get('category')
        subCategory=rp.get('subCat')
        profile.name=name
        profile.category=category
        profile.subCategory=subCategory
        
        return redirect('link:home')


    return render(request,'auth/profile_creation.html',c)