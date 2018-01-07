# coding: utf-8
from django.conf.urls import url

from . import views

app_name = 'JesseJia'

urlpatterns = [


    url(r'^index$', views.index, name='index'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^$', views.login, name='login'),
    url(r'^skeleton$', views.skeleton, name='skeleton'),

    url(r'^aside$', views.aside, name='aside'),
    url(r'^landing$', views.landing, name='landing'),
    url(r'^forum$', views.forum, name='forum'),
    url(r'^hero$', views.hero, name='hero'),
    url(r'^cover$', views.cover, name='cover'),
    url(r'^inbox$', views.inbox, name='inbox'),
]