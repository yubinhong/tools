#!/usr/bin/python
#date: 2019-05-09
#author: ybh
from lxml import etree
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' }
url = "https://ip.cn"
r = requests.get(url,headers=headers)
html = etree.HTML(r.text.encode('utf-8'))
result = html.xpath('//div[@id="result"]/div/p[1]/code[1]/text()')[0]
print(result)
