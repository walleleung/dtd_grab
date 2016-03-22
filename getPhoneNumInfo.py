#-*- coding: utf-8 -*-
import re
import BeautifulSoup
import random
import urllib, httplib 
import urllib2
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from urllib import urlopen
import re
import BeautifulSoup
import random
import urllib, httplib

class PhoneInfoSpider():
    def __init__(self,phoneNum):
        self.url = "https://www.sogou.com/web?query="+str(phoneNum)
        self.text='err' 
    def useragent(self):
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", \
                     "Referer": 'http://sogou.com/'}
        proxy_list=[#代理IP
                    '202.106.169.142:80',
                    '220.181.35.109:8080',
                    '124.65.163.10:8080',
                    '117.79.131.109:8080',
                    '58.30.233.200:8080',
                    '115.182.92.87:8080',
                    '210.75.240.62:3128',
                    '211.71.20.246:3128',
                    '115.182.83.38:8080',
                    '121.69.8.234:8080',
        ]
        proxy = random.choice(proxy_list)
        urlhandle   = urllib2.ProxyHandler({'http':proxy})
        opener = urllib2.build_opener(urlhandle)
        urllib2.install_opener(opener)
        #req = urllib2.Request('https://www.sogou.com/web?query=13022392846', headers=i_headers)
        req = urllib2.Request(self.url, headers=i_headers)
        #content     = urllib2.urlopen(req,timeout=10).read()
        return req
    def enterpage(self):
        req=self.useragent()
        file = urllib2.urlopen(req)
        if file.getcode()==200:
           text = file.read()
           file.close()
           text = text.decode("utf-8")
           soup = BeautifulSoup.BeautifulSoup(text)
           text = str(soup.html.body.find('div', 'vrwrap'))
        else:
           file.close()
        return text
    def getcontent(self,phoneNum):
        text=self.enterpage()
        if text!='err':
           text = text.split((str(phoneNum)))[-1].split('");')[0].split(' ')
           if len(text)>1:
              if len(text)>7:
                 text[0] = text[0][7:]+'市'
                 text[-1] = text[0][1:7]+'省'
              else:
                 text[0] = text[0][1:7]+'市'
                 text[-1] = text[0]
              print text[0], text[1], text[2]
        return text
    def SaveRssFile(self,filename):
        finallxml=self.myrss.to_xml(encoding='utf-8')
        file=open(self.xmlpath,'w')
        file.writelines(finallxml)
        file.close()
'''
def getPhoneInfo(url,phoneNum):
	#url = "https://www.sogou.com/web?query=%s" %phoneNum
        url = url+"%s" %phoneNum
        print url 
        #file = urlopen(url)
        proxy_list=[#这是我当时用的代理IP，请更新能用的IP
                    '202.106.169.142:80',   
                    '220.181.35.109:8080',  
                    '124.65.163.10:8080',
                    '117.79.131.109:8080',
                    '58.30.233.200:8080',
                    '115.182.92.87:8080',
                    '210.75.240.62:3128',
                    '211.71.20.246:3128',
                    '115.182.83.38:8080',
                    '121.69.8.234:8080',
        ]
        #接着在你使用的到urllib2的代码中，绑定某个IP，如下：
        proxy       = random.choice(proxy_list)
        urlhandle   = urllib2.ProxyHandler({'http':proxy})
        opener      = urllib2.build_opener(urlhandle)        
        urllib2.install_opener(opener)
        req         = urllib2.Request(url,headers=header)
        httplib.HTTPConnection.debuglevel = 1
        file = urllib.urlopen(url)
        if file.getcode()==200: 
	   text = file.read()
	   file.close()
	   text = text.decode("utf-8")
           soup = BeautifulSoup.BeautifulSoup(text)
           text = str(soup.html.body.find('div', 'vrwrap')).split((str(phoneNum)))[-1].split('");')[0].split(' ')
           if len(text)>1:
              if len(text)>7:
                 text[0] = text[0][7:]+'市'
                 text[-1] = text[0][1:7]+'省'
              else:
                 text[0] = text[0][1:7]+'市'
                 text[-1] = text[0]
              print text[0], text[1], text[2]
           else:
              pass
        else:
           file.close()
        return text

#getPhoneInfo(url,str(i[0])+str(random.randint(1000,9999)))
'''
if __name__ == "__main__":
    url = "https://www.sogou.com/web?query="
    #getPhoneInfo(url,str(i[0])+str(random.randint(1000,9999)))
    #getPhoneInfo(url,13022392846)
    phoneInfoSpider=PhoneInfoSpider(13022392846)
    phoneInfoSpider.getcontent(13022392846)
    
