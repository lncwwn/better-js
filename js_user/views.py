from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from js_user.models import JsUser


# user signup
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if password == password_confirm:
            js_user = JsUser.objects.create_user(name, password, email)
            js_user.save()
            #send_mail('Subject here', 'Here is the message.', 'postmanager@recursion.cn', ['lncwwn@163.com'], fail_silently=False)
            return HttpResponseRedirect('/')

    return render_to_response('user/signup.html', RequestContext(request))


# user login
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        remember = request.POST['remember']


    return render_to_response('user/login.html')


# user change password
def change_password(request):
    if request.method != 'POST':
        return render_to_response('user/change_password.html')