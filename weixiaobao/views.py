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
reload(sys)
sys.setdefaultencoding('utf8')
# Create your views here.
wxb_count=0
run_flag=False
source='微小宝'
class collectThread(threading.Thread):
    def __init__(self,type,url):
        threading.Thread.__init__(self)
        self.type=type
        self.url=url
    def collect(self,url):
        global source
        global run_flag
        ct=getHtmlWithRefer(url,'http://hao.wxb.com/')
        soup=BeautifulSoup(ct)
        lis=soup.find('ul',attrs={'class':'list-channel'}).find_all('li')
        for li in lis:
            try:
                if run_flag==False:
                    print 'stop'
                    return
                name=li.find('h4').find('span').get_text()
                num=li.find('p',attrs={'class':'text-muted'}).get_text()
                desc=li.find('div',attrs={'class':'media-info'}).find_all('p')[2].get_text()[5:]
                readcount=li.find('div',attrs={'class':'media-info'}).find_all('p')[1].get_text()[10:]
                imgsrc=li.find('img',attrs={'class':'static-img-qrcode'})['src']
                print 'src:%s'%imgsrc
                p=public()
                p.num=num
                p.source=source
                p.name=name
                p.readcount=readcount
                p.desc=desc
                p.type=self.type
                p.url=self.url
                p.addtime=timezone.now()
                p.qrcode=getImgBase64(imgsrc)
                p.save(force_insert=True)
            except Exception,e:
                print e
                pass
    def getTotal(self,url):
        ct=getHtmlWithRefer(url,'http://hao.wxb.com/')
        soup=BeautifulSoup(ct)
        total=soup.find('a',attrs={'class':'nextprev'}).previous_sibling.previous_sibling.get_text()
        return total
    def run(self):
        t=self.getTotal(self.url)
        print 'total:%s'%t
        self.collect(self.url)
        for i in range(2,int(t)):
            self.collect(self.url+'&page='+str(i))
        print 'end'
def start_collect(request):
    global wxb_count
    global run_flag
    if run_flag==True:
        return HttpResponse('0')
    run_flag=True

    print 'start_collect'
    wxb_count=wxb_count+1
    context=getHtml('http://hao.wxb.com/')
    soup=BeautifulSoup(context)
    types=soup.find('ul',attrs={"class": "list-icon clearfix"}).find_all('a')
    for type in types:
        t=collectThread(type.get_text(),type['href'])
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
class PublicListViewWxb(PublicListView):
    def get_template_names(self):
        return ['weixiaobao/public_list_wxb.html']

