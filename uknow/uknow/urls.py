# -*- coding: utf-8 -*-

"""uknow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from django.views.decorators.csrf import csrf_exempt

from users import views as users
from poems import views as poems
from editor import views as editor


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', users.login, name='login'),
    url(r'^login/', users.login, name='login'),
    url(r'^logout', users.logout, name='logout'),
    url(r'^logout/', users.logout, name='logout'),
    url(r'^home', users.home, name='home'),
    url(r'^home/', users.home, name='home'),
    url(r'^poem/new', poems.new, name='new'),
    url(r'^poem/new/', poems.new, name='new'),

    url(r'api/v1/editor/preview', csrf_exempt(editor.api_preview)),
    url(r'api/v1/editor/preview/', csrf_exempt(editor.api_preview)),
    url(r'editor/backbone', csrf_exempt(editor.editor_backbone_view), name='editor_backborn'),
    url(r'editor/backbone/',  csrf_exempt(editor.editor_backbone_view), name='editor_backborn'),
    url(r'editor', csrf_exempt(editor.editor_view), name='editor'),
    url(r'editor/', csrf_exempt(editor.editor_view), name='editor'),
]
