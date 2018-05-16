#ins robots, main script
#coding='utf-8'
#__author__=='0han'
#__email__=='0han@protonmail.com'
#__data__=='2018.5'
import requests,re,json,time,os,os.path,sys
from random import *
from bs4 import BeautifulSoup
import proxy
import dic
import get_pic
#数据

USE_PROXY = False

class register():
		_session=None
		
		def __init__(self):
			self.use_proxy=proxy.get_proxy("US") if USE_PROXY else None
			print("==Instagram-robots-account-generate==\n[*] start")#可以删除
			
		def first_get(self):
			global _session
			_session=requests.session()
			main_url='https://www.instagram.com'
			try:
				_session.get(main_url,proxies=self.use_proxy,verify=True)
				self.save_cookies()
				if os.path.exists('cookiefile'):#print('have cookies')
					self.csrf=self.read_cookies()
					self.data=self.create_ajax()
					print(self.data)
					self.ins()
					time.sleep(5)#wait for 5 seconds
					self.my_selfie=get_pic.get_pic()#实例化——头像-轮子
					self.my_selfie.get_selfie()#download random selfie picture to local folder
					self.upload()#upload the selfie
				else:
					pass
			except:
				print("invalid proxy ip!")
				pass
		def get_emailaddress(self):#获取新的邮箱地址
			email_url="https://10minutemail.net"
			r=requests.get(email_url,verify=True)
			r.encoding='utf-8'
			soup = BeautifulSoup(r.text, 'html.parser')
			return soup.input["value"]
		def generate_FullName(self):
			nameList=dic.data['name']#储存在dic里的姓名数据
			name=nameList[randint(1,12)]
			return name
		def create_username(self):
			username_url="http://namegenerators.org/username-generator/"
			data={'keyword':self.f_name,"numlines":"70","formsubmit":"Generate Username"}
			r=requests.post(username_url,data=data,verify=True)
			r.encoding='utf-8'
			soup=BeautifulSoup(r.text,'html.parser')
			result=soup.select(".section > div:nth-of-type("+str(randint(1,69))+")")[0].string
			result=str(result)+"user"+str(randint(1,2000))
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
		def save_account_info(self,username,password):
			with open("account_info.py", "a+") as a:
			    a.write("\n['"+username+"','"+password+"'],")
			print("[*] Successful save the account info")
		def upload(self):
			global _session
			file={"file":open("selfie/1.jpg","rb")}
			post_selfie_url="https://www.instagram.com/accounts/web_change_profile_picture/"
			data={
				"Content-Disposition":["form-data","name='profile_pic'","filename='profilepic.jpg'"],
				"Content-Type":"image/jpg"
			}
			header={
				"Accept":"*/*",
				"accept-encoding":"gzip, deflate, br",
				"Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryElZwUj6xt3tDzqBy",
				"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
				"origin":"https://www.instagram.com",
				"referer":"https://www.instagram.com/",
				"user-Agent":dic.data["user_agent"],
				"X-csrftoken":self.csrf,
				"X-Instagram-AJAX":"1",
				"X-Requested-With":"XMLHttpRequest",
				}
			r=requests.post(post_selfie_url,headers=header,proxies=self.use_proxy,data=data,files=file,verify=True)
			print(r)
		def ins(self):
			global _session
			posturl='https://www.instagram.com/accounts/web_create_ajax/'
			header={
				"Accept":"*/*",
				"accept-encoding":"gzip, deflate, br",
				"Content-Type":"application/x-www-form-urlencoded",
				"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
				"origin":"https://www.instagram.com",
				"referer":"https://www.instagram.com/",
				"user-Agent":dic.data["user_agent"],
				"X-csrftoken":self.csrf,
				"X-Instagram-AJAX":"1",
				"X-Requested-With":"XMLHttpRequest",
				}		
			r = _session.post(posturl,data=self.data,headers=header,proxies=self.use_proxy,verify=True)#proxies=self.use_proxy
			if r.ok==True:
				print("[*] Sucessful create an account")
				self.save_account_info(self.u_name,self.passwd)
			else:
				print("[x] Unknown Error Occurs!")

test=register()
for i in range(5):
	test.first_get()
	time.sleep(15)
