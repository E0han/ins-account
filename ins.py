#ins robots
import requests,re,json,time,os,os.path,sys
from random import *
from bs4 import BeautifulSoup
import proxy

class register():
		_session=None
		
		def __init__(self):
			self.use_proxy=proxy.get_proxy(3)
			print("==Instagram-robots-account-generate==\n[*] start")#可以删除
			self.first_get()
		def first_get(self):
			global _session
			_session=requests.session()
			main_url='https://www.instagram.com'
			_session.get(main_url,verify=True)
			self.save_cookies()
			if os.path.exists('cookiefile'):#print('have cookies')
				self.csrf=self.read_cookies()
				self.data=self.create_ajax()
				print(self.data)
				self.ins()
			else:
				pass
		def get_emailaddress(self):#获取新的邮箱地址
			email_url="https://10minutemail.net"
			r=requests.get(email_url,verify=True)
			r.encoding='utf-8'
			soup = BeautifulSoup(r.text, 'html.parser')
			return soup.input["value"]
		def generate_FullName(self):
			nameList=["James","Oliver","William","Jack","Noah","Thomas","Lucas","Isaac","Ethan","Alexander","Jacob","Lachlan","Samuel","Harrison","Joshua"]
			name=nameList[randint(1,10)]
			return name
		def create_username(self):
			username_url="http://namegenerators.org/username-generator/"
			data={'keyword':self.f_name,"numlines":"20","formsubmit":"Generate Username"}
			r=requests.post(username_url,data=data,verify=True)
			r.encoding='utf-8'
			soup=BeautifulSoup(r.text,'html.parser')
			result=soup.select(".section > div:nth-of-type("+str(randint(1,20))+")")[0].string
			result=str(result)+"usery"
			return result
		
		def create_ajax(self):
			self.email=self.get_emailaddress()
			self.f_name=self.generate_FullName()
			self.passwd=self.f_name+'password'
			self.u_name=self.create_username()
			r_data={
				'email': self.email, #注册邮箱
				'password': self.passwd,#密码
				'username':self.u_name,#账号（不能重复）
				'first_name': self.f_name#全名
				}
			return r_data
		def save_cookies(self):
			global _session,path_for
			with open('./'+"cookiefile",'w')as f:
				json.dump(_session.cookies.get_dict(),f)#_session.cookies.save()
		def read_cookies(self):
			global _session,path_for
			#_session.cookies.load()
			#_session.headers.update(header_data)
			with open('./'+'cookiefile')as f:
				cookie=json.load(f)
				_session.cookies.update(cookie)
				return cookie["csrftoken"]
		def ins(self):
			global _session
			posturl='https://www.instagram.com/accounts/web_create_ajax/'
			user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
			header={
				"Accept":"*/*",
				"accept-encoding":"gzip, deflate, br",
				"Content-Type":"application/x-www-form-urlencoded",
				"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
				"origin":"https://www.instagram.com",
				"referer":"https://www.instagram.com/",
				"user-Agent":user_agent,
				"X-csrftoken":self.csrf,
				"X-Instagram-AJAX":"1",
				"X-Requested-With":"XMLHttpRequest",
				}		
			r = _session.post(posturl,data=self.data,headers=header,verify=True)#proxies=self.use_proxy
			print(r)

test=register()
