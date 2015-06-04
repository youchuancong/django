# coding=utf-8
from django.db import models
import sys
from datetime import  *
from django.forms import ModelForm
reload(sys)
sys.setdefaultencoding('utf8')
# Create your models here.
#公众号
class public(models.Model):
    num=models.CharField(max_length=128,primary_key=True)#微信号
    name=models.CharField(max_length=256)#名称
    isattention=models.BooleanField(default=False)#是否被关注
    ishello=models.BooleanField(default=False)#是否发送hello消息
    source=models.CharField(max_length=64)#采集入口
    type=models.CharField(max_length=64,null=True)#行业类型
    url=models.CharField(max_length=256)#采集到该公众号的页面地址
    qq=models.CharField(max_length=32,null=True)#qq号
    phone=models.CharField(max_length=32,null=True)#联系电话
    desc=models.CharField(max_length=128,null=True)#描述
    readcount=models.IntegerField(null=True)#阅读数量
    addtime=models.DateTimeField(null=True)#添加时间
    qrcode=models.TextField(null=True)#二维码base64值

def getPublicCounts(source=''):
    if source=='':
        return public.objects.filter().count()
    else:
        return public.objects.filter(source=source).count()
def getPublicTodays(source=''):
    td=date.today()
    if source=='':
        return public.objects.filter(addtime__gte=td).count()
    else:
        return public.objects.filter(source=source).filter(addtime__gte=td).count()
#关注公众号用的微信号
class webchat(models.Model):
    num=models.CharField(max_length=32,primary_key=True)#微信号
    pwd=models.CharField(max_length=32)#密码
    isuse=models.BooleanField(default=False)#当前是否正在使用 true:已经登录  false:未登录
    isblock=models.BooleanField(default=False)#是否被封号 true:被封号 false:未封，可正常使用
    updatetime=models.DateTimeField(null=True)#更新时间
    lastusetime=models.DateTimeField(null=True)#更新时间
    def __unicode__(self):
        return self.num
    def normalCount(self):
        return webchat.objects.filter(isblock=False).count()
    def blockCount(self):
        return webchat.objects.filter(isblock=True).count()
    class Meta:
        ordering = ["-updatetime"]

class webchatForm(ModelForm):
    class Meta:
        model = webchat
        fields = ['num', 'pwd']
        labels = {
            'num': ('微信帐号'),
            'pwd': ('密码'),
        }
#打招呼模版
class hellomsg(models.Model):
    context=models.CharField(max_length=128)#内容
    isactive=models.BooleanField(default=True)#是否为活跃状态，活跃的打招呼语数量不超过4

#公众号回复的消息
class resmsg(models.Model):
    num=models.ForeignKey(public)#公众号的微信号
    context=models.CharField(max_length=256)#内容
    time=models.DateTimeField()#时间

