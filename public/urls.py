from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^index/$', views.index, name='index'),
    url(r'^csv/$', views.some_view, name='csv'),
    url(r'^webchats/$', views.WebChatListView.as_view(),name='webchatlist'),
    url(r'^publics/$', views.PublicListViewAll.as_view(),name='publiclist_all'),
    url(r'^public_detail/$', views.public_detail,name='public_detail'),
    url(r'^addwebchat/$', views.add_webchat,name='addwebchat'),
    url(r'^del_webchat/$',views.del_webchat,name='del_webchat'),
    url(r'^login/$',views.login_action,name='login_action'),
    url(r'^get_active_webchat/(?P<count>[0-9]+)/$', views.get_active_webchat, name='get_active_webchat'),
    url(r'^release_webchat/(?P<num>\w+)/$', views.release_webchat, name='release_webchat'),
    url(r'^block_webchat/(?P<num>\w+)/$', views.block_webchat, name='block_webchat'),
    url(r'^unblock_webchat/(?P<num>\w+)/$', views.unblock_webchat, name='unblock_webchat'),
    url(r'^get_publics/(?P<count>[0-9]+)/$', views.get_publics, name='get_publics'),
    url(r'^upload_public_res/$', views.upload_public_res, name='upload_public_res'),

    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
