from django.shortcuts import render
from .models import register, blog_post1
# Create your views here.

def index(request):
    return render(request, 'index.html')


def regist(request):
    if (request.method == "POST"):
        if ((request.POST.get('uname')) and (request.POST.get('name')) and (request.POST.get('pwd')) and (
        request.POST.get('mob')) and (request.POST.get('email')) and (request.POST.get('question')) and(request.POST.get('answer'))):
            obj = register()
            obj.uname = request.POST.get('uname')
            obj.name = request.POST.get('name')
            obj.pwd = request.POST.get('pwd')
            obj.mobile = request.POST.get('mob')
            obj.email = request.POST.get('email')
            obj.question = request.POST.get('question')
            obj.answer = request.POST.get('answer')
            obj.save()
            return render(request,'index.html')
    else:
        return render(request,'register.html')


def login(request):
    if (request.method == "POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        obj=register.objects.get(uname=username, pwd=password)
        if obj:
            request.session['name']=obj.name
            request.session['user']= username

            return render(request, 'user.html')
        else:
                return render(request, 'login.html')


    else:
        return render(request, 'login.html')


def rstpwd(request):
    if (request.method == "POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        try:
            if register.objects.get(uname=username, pwd=password):
                npwd = request.POST.get('passn')
                register.objects.filter(uname=username).update(pwd=npwd)
                return render(request, 'index.html')
        except register.DoesNotExist:
            return render(request, 'rp.html')
    else:
        return render(request, 'rp.html')


def cblog(request):
    if (request.method == "POST"):
        if ((request.POST.get('bname'))and (request.POST.get('blog'))):

            obj = blog_post1()
            obj.username = request.session['user']
            obj.bname = request.POST.get('bname')
            obj.author = request.session['name']
            obj.blog = request.POST.get('blog')
            obj.save()
            user = request.session['user']
            userblog = blog_post1.objects.filter(username=user)
            return render(request, 'vblog.html', {'blogs': userblog})
        else:
            return render(request,'')

    else:
        return render(request, 'blog.html')


def logout(request):
    try:
        del request.session["user"]
    except:
        pass
    return render(request, 'login.html')


def viewBlog(request):
    user = request.session['user']
    userblog = blog_post1.objects.filter(username=user)
    return render(request, 'vblog.html', {'blogs': userblog})


def viewallblogs(request):
    allblog = blog_post1.objects.all()
    return render(request, 'vablog.html', {'blogs': allblog})

def editBlog(request, pk):
    l = blog_post1.objects.filter(id =pk)
    print(l)
    return render(request, 'editblog.html', {'blogs': l})


def update(request):
    if (request.method == "POST"):
        title = request.POST.get('title')
        blog = request.POST.get('content')
        id=request.POST.get('hid')
        blog_post1.objects.filter(id=id).update(bname=title)
        blog_post1.objects.filter(id=id).update(blog=blog)
        user = request.session['user']
        userblog = blog_post1.objects.filter(username=user)
        return render(request, 'vblog.html', {'blogs': userblog})




