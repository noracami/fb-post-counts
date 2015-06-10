"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pages.views import home, page_list, page_item_detail, page_item_create, page_item_update

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^page/$', page_list, name='page_list'),
    url(r'^page/(?P<pk>\d+)/$', page_item_detail, name='page_item_detail'),
    url(r'^page/new/$', page_item_create, name='page_item_create'),
    url(r'^page/(?P<pk>\d+)/update/$', page_item_update, name='page_item_update'),
    url(r'^admin/', include(admin.site.urls)),
]
