# -*- coding: utf-8 -*-

from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse # TODO
from django.http import HttpResponseRedirect

from users.forms import LoginForm

@require_http_methods(['GET', 'POST'])
def login(request):
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'users/home.html')

        return render_to_response('users/login.html', context_instance = RequestContext(request, {'form': form}))

    elif (request.method == 'GET'):
        form = LoginForm()
        return render_to_response('users/login.html', context_instance = RequestContext(request, {'form': form}))

    else:
        raise Http404('Does not page exist.')

@require_http_methods(['POST'])
def logout(request):
    if (request.method == 'POST'):
        auth.logout(request)
        form = LoginForm()
        return render_to_response('users/login.html', context_instance = RequestContext(request, {'form': form}))

@require_http_methods(['GET'])
def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'users/home.html')

    form = LoginForm()
    return render_to_response('users/login.html', context_instance = RequestContext(request, {'form': form}))
