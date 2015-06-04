from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^start_collect/$', views.start_collect, name='wxb_start_collect'),
    url(r'^stop_collect/$', views.stop_collect, name='wxb_stop_collect'),
    url(r'^isrunning/$', views.isRunning, name='wxb_collect_isrunning'),
    url(r'^publics_wxb/$', views.PublicListViewWxb.as_view(),name='publiclist_wxb'),
]
