from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index_view(request):
    if request.method == 'GET':
        if 'user' in request.session:
            is_not_login = False
            name = request.session['user']['name']
        else:
            is_not_login = True
        return render(request, 'index/index.html', locals())
