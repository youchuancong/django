from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^start_collect/$', views.start_collect, name='xmt_start_collect'),
    url(r'^stop_collect/$', views.stop_collect, name='xmt_stop_collect'),
    url(r'^isrunning/$', views.isRunning, name='xmt_collect_isrunning'),
    url(r'^publics_xmt/$', views.PublicListViewXmt.as_view(),name='publiclist_xmt'),
]
