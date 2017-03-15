# coding=utf-8
'''类名称
描述:
包含方法：
'''
__author__ = 'ShaYuan'

from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CiWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),

)
