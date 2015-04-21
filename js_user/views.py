from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template


def signup(request):
    if request.method != 'POST':
        return render_to_response('user/signup.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            pass
        else:
            tmplt = get_template('user/signup.html')
            html = tmplt.render(RequestContext(request, None))
            return HttpResponse(html)


def signin(request):
    if request.method != 'POST':
        return render_to_response('user/signin.html')


def change_password(request):
    if request.method != 'POST':
        return render_to_response('user/change_password.html')