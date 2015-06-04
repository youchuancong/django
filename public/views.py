#!coding=UTF-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
import time
import csv
import sys
import logging
from django.shortcuts import redirect
from django.views.generic import ListView
from public.models import webchat,webchatForm,public,getPublicCounts,getPublicTodays,resmsg
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
reload(sys)
sys.setdefaultencoding('utf8')
logger = logging.getLogger(__name__)
# Create your views here.
@login_required
def index(request):
    return render(request,'public/index.html')

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
#获取活跃可用的微信号
def get_active_webchat(request,count=1):
    objs=webchat.objects.filter(isuse=False,isblock=False)[:count]
    rows=[]
    for obj in objs:
        rows.append({'num':obj.num,'pwd':obj.pwd})
        obj.isuse=True
        obj.lastusetime=timezone.now()
        obj.save()
    return JsonResponse({'total':len(rows),'rows':rows})
#释放微信号，继续可供其它客户端使用
def release_webchat(request,num):
    try:
        chat=webchat.objects.get(num=num)
        chat.isuse=False
        chat.save()
    except Exception,e:
        logger.error('error '+e.message)
    return HttpResponse('0')
#锁定微信号，被封
def block_webchat(request,num):
    logger.error('logger errer test')
    try:
        chat=webchat.objects.get(num=num)
        chat.isblock=True
        chat.save()
    except Exception,e:
        logger.error('error '+e.message)
    return HttpResponse('0')
#获取公众号
def get_publics(request,count=10):
    logger.debug('start')
    try:
        pubs=public.objects.filter(isattention=False)[:count]
        rows=[]
        for pub in pubs:
            rows.append({'num':pub.num,'name':pub.name})
            pub.isattention=True
            pub.save()
        logger.debug(rows)
        return JsonResponse({'total':len(rows),'rows':rows})
    except  Exception,e:
        logger.error('error '+e.message)
    logger.debug('end')
#上传公众号回复信息
@csrf_exempt
def upload_public_res(request):
    logger.debug('start')
    try:
        num=request.POST.get('num')
        context=request.POST.get('context')
        pub=public.objects.get(num=num)
        pub.ishello=True
        pub.save()
        rs=resmsg()
        rs.num=pub
        rs.context=context
        rs.time=timezone.now()
        rs.save()
        return HttpResponse('0')
    except Exception,e:
        logger.error('error '+e.message)
        return HttpResponse('1')
    logger.debug('end')

def unblock_webchat(request,num):
    try:
        chat=webchat.objects.get(num=num)
        chat.isblock=False
        chat.save()
    except Exception,e:
        print e
    return HttpResponse('0')
def del_webchat(request):
    num=request.GET.get('num')
    webchat.objects.filter(num=num).delete()
    return HttpResponse("0")
def add_webchat(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        num=request.POST.get('num')
        ins=webchat.objects.filter(num=num)
        if len(ins)>0:
            form = webchatForm(request.POST,instance=ins[0])
        else:
            form=webchatForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('public/thanks/')
            wc=form.save(commit=False);#此处不提交，可更改其它值再行提交
            wc.updatetime=timezone.now()
            wc.save()
            return HttpResponse("0")

    # if a GET (or any other method) we'll create a blank form
    else:
        num=request.GET.get('num')
        form = webchatForm()
        if not num==None:
            ins=webchat.objects.get(num=num)
            form = webchatForm(instance=ins)
        return render(request, 'public/add_webchat.html', {'form': form})

class PublicListView(ListView):
    model = public
    context_object_name = 'msg_list'#模板中变量
    paginate_by = 20#一个页面显示的条目
    ordering='-addtime'
    template_name = 'public/public_list.html'#模板文件
    def get_queryset(self):
        source=self.request.GET.get('source')
        if source==None or source=='all':
            list=public.objects.order_by(self.ordering)
        else:
            list=public.objects.filter(source=source).order_by(self.ordering)
        return list

    def get_context_data(self, **kwargs):
        context = super(PublicListView,self).get_context_data(**kwargs)
        source=self.request.GET.get('source')
        if source=='all':
            context['total']=getPublicCounts()
            context['today']=getPublicTodays()
        else:
            context['total']=getPublicCounts(source)
            context['today']=getPublicTodays(source)
        context['source']=source
        return context
def public_detail(request):
    num=request.GET.get('num')
    try:
        data=public.objects.get(num=num)
    except Exception,e:
        print e
    return render(request, 'public/public_detail.html', {'data': data})
class PublicListViewAll(PublicListView):
    def get_template_names(self):
        return ['public/public_list_all.html']
class WebChatListView(ListView):
    model = webchat
    ordering='updatetime'
    context_object_name = 'msg_list'#模板中变量
    #template_name = 'public/aaaa.html'#模板文件
    paginate_by = 20#一个页面显示的条目
    def get_queryset(self):#搜索条件
        list = webchat.objects.order_by('-updatetime')
        #plat = self.request.GET.get('plat')
        #keyword = self.request.GET.get('keyword')
        return list
    def get_context_data(self, **kwargs):
        context = super(WebChatListView,self).get_context_data(**kwargs)
        web=webchat()
        context['nomalCount']=web.normalCount()
        context['blockCount']=web.blockCount()
        return context
    def head(self, *args, **kwargs):
        #last_book = self.get_queryset().latest('publication_date')
         response = HttpResponse('')
        # RFC 1123 date format
       # response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
         return response
def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return  redirect(reverse('index', args=[]))
        else:
            # Return a 'disabled account' error message
            print 'login success'
    else:
        # Return an 'invalid login' error message.
        print 'login error'
        pass