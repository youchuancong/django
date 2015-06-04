#coding=utf-8
import urllib2
import sys
import base64
import requests
reload(sys)
sys.setdefaultencoding('utf8')
#以urllib2实现存在不支持长连接的问题
'''
def getHtml(url,charset='utf-8'):
    req = urllib2.Request(url)
    page = urllib2.urlopen(req)
    html = page.read().decode(charset,'ignore')
    return html
def getHtmlWithRefer(url,refer,charset='utf-8'):
    req = urllib2.Request(url)
    req.add_header('Referer',refer)
    page = urllib2.urlopen(req)
    html = page.read().decode(charset,'ignore')
    return html
def getImgBase64(url):
    page = urllib2.urlopen(url)
    return base64.b64encode(page.read())
'''
def getHtml(url,charset='utf-8'):
    req = requests.get(url)
    return req.text
def getHtmlWithRefer(url,refer,charset='utf-8'):
    headers = {'Referer':refer}
    req = requests.get(url,headers=headers)
    return req.text
def getImgBase64(url):
    req = requests.get(url)
    return base64.b64encode(req.content)
