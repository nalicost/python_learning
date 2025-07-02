from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F, Q
from . import models

# Create your views here.


def m_price_filter(query_object, value):
    value = value[1]
    if value[0] == "+":
        query_object = query_object & models.Book.objects.filter(market_price__gt=int(value[1:]))
    elif value[0] == "-":
        query_object = query_object & models.Book.objects.filter(market_price__lt=int(value[1:]))
    else:
        raise ValueError
    return query_object


def tit_filter(query_object, value):
    value = value[1]
    query_object = query_object & models.Book.objects.filter(title__contains=value)
    return query_object


def publisher_filter(query_object, value):
    value = value[1]
    query_object = query_object & models.Book.objects.filter(title__contains=value)
    return query_object


def rise_fall_filter(query_object, value):
    value = value[1]
    if value[0] == "+":
        query_object = query_object & models.Book.objects.filter(market_price__gt=F("price"))
    elif value[0] == "-":
        query_object = query_object & models.Book.objects.filter(market_price__lt=F("price"))
    else:
        raise ValueError
    return query_object


def index_view(request):
    if request.method == "GET":
        iter_re = models.Book.objects.all()
        return render(request, "bookstore/bookstore_index.html", locals())
    elif request.method == "POST":
            rq_dict = dict(request.POST)
            iter_re = models.Book.objects.all()
            filter_select_dict = {"m_price": m_price_filter,
                                  "tit": tit_filter,
                                  "publisher": publisher_filter,
                                  "rise_fall": rise_fall_filter}
            for key in rq_dict.keys():
                value = rq_dict[key]
                if value[0] == "1":
                    iter_re = filter_select_dict[key](iter_re, value)
            return render(request, "bookstore/bookstore_index.html", locals())



def add_view(request):
    if request.method == "GET":
        return render(request, "bookstore/bookstore_add.html")
    elif request.method == "POST":
        try:
            rq_dict = dict(request.POST)
            models.Book.objects.create(title=rq_dict['title'][0],
                                       price=abs(round(float(rq_dict['price'][0]), 2)),
                                       pub=rq_dict['pub'][0],
                                       market_price=abs(round(float(rq_dict['market_price'][0]), 2)))
            return HttpResponseRedirect("/bookstore/")
        except Exception:
            return HttpResponse("<h1 style='color: red;font-weight: bold'>请输入正确的值</h1>")


def modify_view(request, book_id):
    if request.method == "GET":
        item = models.Book.objects.get(id=book_id)
        return render(request, "bookstore/bookstore_mod.html", locals())
    elif request.method == "POST":
        try:
            rq_mod = abs(round(float(request.POST['market_price'])))
            abook = models.Book.objects.get(id=book_id)
            abook.market_price = rq_mod
            abook.save()
            return HttpResponseRedirect("/bookstore/")
        except Exception:
            return HttpResponse("<h1 style='color: red;font-weight: bold'>请输入正确的值</h1>")


def del_view(request, book_id):
    if request.method == "GET":
        abook = models.Book.objects.get(id=book_id)
        abook.delete()
        return HttpResponseRedirect("/bookstore/")


def filter_view(request):
    if request.method == "GET":
        return render(request, "bookstore/bookstore_filter.html")
