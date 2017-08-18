#Get_Proxy_list by 0han
#date="2017.4.29"
#coding:utf-8 python 3.5 
import requests
from bs4 import BeautifulSoup
import time

def get_proxy(n):
	proxy_dic={}
	proxy={}
	url='http://www.kuaidaili.com/free/'
	req=requests.get(url)
	soup = BeautifulSoup(req.text,'html.parser')
	for i in range(1,n):
		IP=soup.select("#list > table > tbody > tr:nth-of-type("+str(i)+") > td:nth-of-type(1)")[0].string
		PORT=soup.select("#list > table > tbody > tr:nth-of-type("+str(i)+") > td:nth-of-type(2)")[0].string			
		print("[*]已成功获取代理ip Get IP proxy "+IP+" successfully")
		proxy_dic["http"]='http://'+IP+':'+PORT		
		time.sleep(1)
	return proxy_dic

