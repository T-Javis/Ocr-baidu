# -*- coding: utf-8 -*-
# python apistore.py < ocr.jpg

from base import BaseModel
import json
from bs4 import BeautifulSoup

def dal():
	return BaseModel()
db = dal().db

data_db = db.query('select * from test1')


import sys, urllib, urllib2, json, base64
url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "10.10.10.0"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"
data['version'] = "v2"
data['sizetype'] = "big"


file=open('ocr_test10.png','rb')
image=file.read()
file.close


data['image']=base64.b64encode(image)
print(data['image'])
decoded_data = urllib.urlencode(data)
req = urllib2.Request(url, data = decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("apikey", "8240******fa339")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
db.execute('update test1 set content_json=%s where id=%s',(content,10))

