#ins robots, main script
#coding='utf-8'
#__author__=='0han'
#__email__=='0han@protonmail.com'
#__data__=='2017.8'
import requests,re,json,time,os,os.path,sys
from data import header, name
from random import randint
from bs4 import BeautifulSoup
from proxy import proxy_pool
#数据
class login(object):
	def __init__(self, proxy, accountlist, session):
		self.list=accountlist
		self.proxy=proxy
		self._session=session
	def run(self):
		self._session.get('https://www.instagram.com',verify=True)#proxies=self.proxy
		self.save_cookies()
		header['cookie']=str(self.read_cookies())[1:-2]
		header['X-csrftoken']=self.read_cookies()["csrftoken"]
		self.login()
	def login(self):
		for i in self.list:
			self.u_name=i[0]
			self.passwd=i[1]
			payload=self.create_ajax()
			r = self._session.post('https://www.instagram.com/accounts/login/ajax/',data=payload,headers=header,verify=True)#proxies=self.proxy
			if r.ok==True:
				self.save_cookies()
				print("[*] Sucessful log in to the",self.u_name)
			else:
				print("[x] Unknown Error Occurs!")
	def create_ajax(self):
		r_data={
			'username':self.u_name,#username
			'password': self.passwd,#password
			}
		return r_data
	def save_cookies(self):
		with open('./'+"cookiefile",'w')as f:
			json.dump(self._session.cookies.get_dict(),f)#_session.cookies.save()
	def read_cookies(self):
		#_session.cookies.load()
		#_session.headers.update(header_data)
		with open('./'+'cookiefile')as f:
			cookie=json.load(f)
			self._session.cookies.update(cookie)
			return cookie
