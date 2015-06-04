"""weixin URL Configuration

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
from django.views.generic import TemplateView
'''
    url(r'^admin/', include(admin.site.urls)),
    url(r'^public/', include('public.urls')),
'''

'''
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^index', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', 'demo_app.views.demo_form'),
    url(r'^form_template$', 'demo_app.views.demo_form_with_template'),
    url(r'^form_inline$', 'demo_app.views.demo_form_inline'),
    url(r'^formset$', 'demo_app.views.demo_formset', {}, "formset"),
    url(r'^tabs$', 'demo_app.views.demo_tabs', {}, "tabs"),
    url(r'^pagination$', 'demo_app.views.demo_pagination', {}, "pagination"),
    url(r'^widgets$', 'demo_app.views.demo_widgets', {}, "widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
'''
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='public/login.html'), name='login'),
    url(r'^public/', include('public.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weixiaobao/', include('weixiaobao.urls')),
    url(r'^xinmeiti/', include('xinmeiti.urls')),
]
