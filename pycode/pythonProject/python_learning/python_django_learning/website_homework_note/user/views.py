from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User

# Create your views here.


def login_view(request):
    is_not_login = True
    if 'user' in request.session:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        user_name = request.COOKIES.get('user', '')
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        user_name = str(request.POST['user'])
        pwd = str(request.POST['password'])
        rem = str(request.POST.get('rem', ''))
        try:
            obj = User.objects.get(name=user_name, password=pwd)
            request.session['user'] = {
                'name': user_name,
                'id': obj.id
            }
            resp = HttpResponseRedirect('/')
            if rem == '1':
                resp.set_cookie('user', user_name)
            return resp
        except Exception:
            errorA = '用户名或密码错误！'
            return render(request, 'user/login.html', locals())


def register_view(request):
    is_not_login = True
    if request.method == 'GET':
        return render(request, 'user/register.html', locals())
    elif request.method == 'POST':
        user_name = str(request.POST['user'])
        pwd = str(request.POST['password'])
        pwd_rp = str(request.POST['pwd_confirm'])
        try:
            User.objects.get(name=user_name)
            errorA = '用户名已存在！'
            return render(request, 'user/register.html', locals())
        except Exception:
            if len(user_name) < 6:
                errorA = '请输入不少于六个长度的用户名！'
                return render(request, 'user/register.html', locals())
            elif len(pwd) < 6:
                errorB = '请输入不少于六个长度的密码！'
                return render(request, 'user/register.html', locals())
            elif pwd != pwd_rp:
                errorB = '两次密码不一致！'
                return render(request, 'user/register.html', locals())
            a_user = User.objects.create(name=user_name, password=pwd)
            resp = HttpResponseRedirect('/')
            resp.set_cookie('user', user_name)
            return resp


def logout_view(request):
    del request.session['user']
    return HttpResponseRedirect('/')
