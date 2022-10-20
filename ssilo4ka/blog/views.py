from django.shortcuts import render as r

def l(request):
    c={}
    return r(request,'b/l.html',c)

def c(request,categorySlug):
    c={}
    return r(request,'blog/category.html',c)

def p(request,postSlug):
    c={}
    return r(request,'blog/posts/post.html',c)
