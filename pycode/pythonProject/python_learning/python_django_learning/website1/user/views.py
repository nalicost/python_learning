from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
# Create your views here.


def index_view(request):
    if request.method == "GET":
        return HttpResponse("这是主页")


def register_view(request):
    is_show_a = 0
    is_show_b = 0
    if request.method == "GET":
        return render(request, "user/register.html", locals())
    elif request.method == "POST":
        re_dict = dict(request.POST)
        if len(re_dict['user'][0]) < 6:
            is_show_a = 1
            return render(request, "user/register.html", locals())
        if models.User.objects.filter(name=re_dict['user'][0]):
            is_show_a = 1
            return render(request, "user/register.html", locals())
        else:
            if re_dict["password"][0] == re_dict["pwd_confirm"][0] and len(re_dict['password'][0]) >= 6:
                re = models.User.objects.filter(name=re_dict['user'][0])
                models.User.objects.create(name=re_dict['user'][0], password=re_dict["password"])
                resp = HttpResponseRedirect("/user/")
                resp.set_cookie(value=re_dict['user'][0], key='user')
                return resp
            else:
                is_show_b = 1
                return render(request, "user/register.html", locals())
