from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import urls as base_urls
from base import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CiWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.log_in, name='login'),
    url(r'^logout/', views.log_out, name='logout'),

    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^charts/', views.charts, name='charts'),
    url(r'^ci/', views.ci, name='ci'),
    url(r'^cd/', views.cd, name='cd'),
    url(r'^settings/', views.settings, name='settings'),


)
