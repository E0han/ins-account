#Get_Proxy_list by 0han
#date="2017.4.29"
#coding:utf-8 python 3.5 
import requests
import json
url="http://gimmeproxy.com/api/getProxy"
s=requests
def get_proxy(country):
	print("[*] Get Annoymous IP Proxy")
	mainurl="https://gimmeproxy.com/api/getProxy?get=true&supportsHttps=true&country="+country
	r=s.get(mainurl)
	dic=json.loads(r.text)
	dic_main={'dic["protocol"]':dic["curl"], 'https':dic["curl"]}
	print(dic_main)
	return dic_main
#list > table > tbody > tr:nth-child(1) > td.style1

def test():
	ip=get_proxy("US")
	url='https://api.ipify.org?format=json'
	res=s.get(url, proxies=ip)
	dic=json.loads(res.text)
	print(dic["ip"])
test()