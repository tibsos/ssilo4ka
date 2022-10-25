from django.shortcuts import render,redirect

def landing(request):
    c={}
    c['authenticated']=request.user.is_authenticated

    if request.method=='POST':
        return redirect('user:landing-register',request.POST.get('username'))

    return render(request,'templates/landing.html',c)
