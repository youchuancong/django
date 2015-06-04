#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
import sys
from django.utils import timezone
import threading
sys.path.append("..")
from public.mytools import  *
from public.models import *
from public.views import PublicListView
from bs4 import BeautifulSoup
from datetime import date,timedelta
reload(sys)
sys.setdefaultencoding('utf8')
# Create your views here.
wxb_count=0
run_flag=False
source='微小宝'
class collectThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.post_url='http://www.newrank.cn/xdnphb/list/day/rank.json'
        self.yesterday=str(date.today()+timedelta(days=-1))
        self.source='新媒体排行榜'
    def rank_post(self,rank_name,rank_name_group):
        payload = {'end': self.yesterday, 'rank_name': rank_name,'rank_name_group':rank_name_group,'start':self.yesterday}
        r = requests.post(self.post_url, data=payload)
        return r.json()
    def get_desc(self,account):
        url='http://www.newrank.cn/xdnphb/data/getByAccount.json'
        data={'account':account}
        r=requests.post(url,data=data)
        return r.json()['value']['user']['description']
    def collect_public(self,d,type):
        try:
            p=public()
            p.num=d['account']
            p.source=self.source
            p.name=d['name']
            p.readcount=d['f']
            p.desc=self.get_desc(d['account'])
            p.type=type
            p.url=self.post_url
            p.addtime=timezone.now()
            p.qrcode=getImgBase64('http://open.weixin.qq.com/qr/code/?username='+d['account'])
            print '公众号:%s  %s'%(p.name,p.num)
            p.save(force_insert=True)
        except Exception,e:
            print e
    def collect_types(self,types,group):
        for type in types:
            if run_flag==False:
                return
            else:
                ds=self.rank_post(type,group)
                for d in ds['value']:
                    if run_flag==False:
                        return
                    else:
                        self.collect_public(d,type)
    def collect_zinxun(self):
        group='资讯'
        types=['时事','民生','财富','科技','创业','汽车','楼市','职场','教育','学术','政务','企业']
        self.collect_types(types,group)
    def collect_life(self):
        group='生活'
        types=['文化','百科','健康','时尚','美食','乐活','旅行','幽默','情感','体娱','美体','文摘']
        self.collect_types(types,group)
    def collect_type_item(self,ulid):
        soup=BeautifulSoup(self.main_context)
        types=soup.find('ul',attrs={"id": ulid}).find_all('a')
        res=[]
        for type in types:
            res.append(type['data'])
        return res
    def run(self):
        global run_flag
        self.collect_zinxun()
        self.collect_life()
        run_flag=False
        print 'end'
def start_collect(request):
    print 'xmt start'
    global run_flag
    if run_flag==True:
        return HttpResponse('0')
    run_flag=True
    t=collectThread()
    t.start()
    return HttpResponse('0')
def stop_collect(request):
    print 'stop_collect'
    global run_flag
    run_flag=False
    return HttpResponse('0')

def isRunning(request):
    global run_flag
    if run_flag==True:
        return HttpResponse('1')
    else:
        return HttpResponse('0')
class PublicListViewXmt(PublicListView):
    def get_template_names(self):
        return ['xinmeiti/public_list_xmt.html']

