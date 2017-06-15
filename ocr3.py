# -*- coding: utf-8 -*-
# python apistore.py < ocr.jpg

from base import BaseModel
import json
from bs4 import BeautifulSoup
import sys, urllib, urllib2, json, base64

def dal():
	return BaseModel()
db = dal().db


def word_info():
	data_db = db.query('select * from test1')

	for i in range(0,len(data_db)):
		data_list=data_db[i]
		data_id=data_list['id']
		data_content_json=data_list['content_json']
		data_name=data_list['name']

		data_content_dict=json.loads(data_content_json)
		data_content_list=data_content_dict['retData']
		examination_report=[]
		for j in range(0,len(data_content_list)):
			data_content=data_content_list[j]
			data_content_word=data_content['word']
			examination_report.append(data_content_word)
			db.execute('update test1 set word=%s where id=%s',(examination_report,data_id))

			print(data_content_word)
		print('-'*10)
	return None	


def ocr():
	url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'

	data = {}
	data['fromdevice'] = "pc"
	data['clientip'] = "10.10.10.0"
	data['detecttype'] = "LocateRecognize"
	data['languagetype'] = "CHN_ENG"
	data['imagetype'] = "1"
	data['version'] = "v2"
	data['sizetype'] = "big"


	for i in range(6,9+1):
		i_str=str(i)
		name='ocr_test'+i_str+'.jpg'
		file=open(name,'rb')
		image=file.read()
		file.close

		data['image']=base64.b64encode(image)
		decoded_data = urllib.urlencode(data)
		req = urllib2.Request(url, data = decoded_data)

		req.add_header("Content-Type", "application/x-www-form-urlencoded")
		req.add_header("apikey", "824*********1e")

		resp = urllib2.urlopen(req)
		content = resp.read()
		if(content):
		    print(content)
		db.execute('update test1 set content_json=%s where id=%s',(content,i))
	return None	



if __name__ == '__main__':
	#ocr()
	word_info()

	print('----------finish---------')

