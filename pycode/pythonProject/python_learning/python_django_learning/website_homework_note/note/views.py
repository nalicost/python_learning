from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Note
from user.models import User
from django.core.paginator import Paginator

# Create your views here.


def is_login(func):
    def wrapper(*args, **kwargs):
        if 'user' in args[0].session:
            return func(*args, **kwargs)
        else:
            return HttpResponseRedirect('/user/login')
    return wrapper


@is_login
def index_view(request):
    name = request.session['user']['name']
    user = User.objects.get(name=name)
    if request.method == 'GET':
        note_all_list = Note.objects.filter(user=user)
        paginator_note = Paginator(note_all_list, 5)
        page_num = int(request.GET.get('page', 1))
        notes = paginator_note.page(page_num)
        return render(request, 'note/index.html', locals())


@is_login
def add_note_view(request):
    name = request.session['user']['name']
    if request.method == 'GET':
        return render(request, 'note/add_note.html', locals())
    elif request.method == 'POST':
        title = str(request.POST['title'])
        content = str(request.POST['content'])
        user = User.objects.get(name=name)
        if not title:
            errorA = '标题不能为空！'
            return render(request, 'note/add_note.html', locals())
        else:
            try:
                Note.objects.get(user=user, title=title)
                errorA = '标题已存在！'
                return render(request, 'note/add_note.html', locals())
            except Exception:
                Note.objects.create(title=title, content=content, user=user)
                return HttpResponseRedirect('/note')


@is_login
def mod_note_view(request, id_):
    name = request.session['user']['name']
    user = User.objects.get(name=name)
    if request.method == 'GET':
        try:
            note = Note.objects.get(user=user, id=id_)
        except Exception:
            return HttpResponseRedirect('/note')
        return render(request, 'note/modify_note.html', locals())
    elif request.method == 'POST':
        note = Note.objects.get(user=user, id=id_)
        new_tit = str(request.POST['title'])
        new_con = str(request.POST['content'])
        note.title = new_tit
        note.content = new_con
        note.save()
        return HttpResponseRedirect('/note')


@is_login
def del_note_view(request, id_):
    name = request.session['user']['name']
    user = User.objects.get(name=name)
    if request.method == 'GET':
        try:
            note = Note.objects.get(user=user, id=id_)
            note.delete()
            return HttpResponseRedirect('/note')
        except Exception:
            return HttpResponseRedirect('/note')

