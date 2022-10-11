from django.shortcuts import render,redirect
def landing(request):

    if request.method=='POST':
        username=request.POST.get('username')
        return redirect('user:landing-register',username=username)

    return render(request,'landing.html')

