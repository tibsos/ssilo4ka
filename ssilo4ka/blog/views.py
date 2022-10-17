from django.shortcuts import render

def landing(request):
    c={}
    return render(request,'blog/landing.html',c)

def category(request,categorySlug):
    c={}
    return render(request,'blog/category.html',c)

def post(request,postSlug):
    c={}
    return render(request,'blog/posts/post.html',c)
