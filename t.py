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

url='https://www.sogou.com/web?query=13022392846'
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
req = urllib2.Request(url, headers=i_headers)
content     = urllib2.urlopen(req,timeout=10).read()
print content
