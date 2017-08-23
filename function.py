#login and function
import account_info
import requests,re,json,time,os,os.path,sys
from random import *
import dic


#数据
user_list=account_info.account
class login():
		_session=None

		def __init__(self):
			pass
		def do_first(self):
			global _session
			_session=requests.session()
			main_url='https://www.instagram.com'
			_session.get(main_url,verify=True)
			self.save_cookies()
			if os.path.exists('cookiefile'):#print('have cookies')
				self.csrf=self.read_cookies()
				self.data=self.create_ajax()
				self.login_now()
			else:
				pass
		def login_now(self):
			global _session
			posturl='https://www.instagram.com/accounts/login/ajax/'
			header={
				"Accept":"*/*",
				"accept-encoding":"gzip, deflate, br",
				"Content-Type":"application/x-www-form-urlencoded",
				"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
				"content-length":"19",
				"origin":"https://www.instagram.com",
				"referer":"https://www.instagram.com/",
				"user-Agent":dic.data["user_agent"],
				"X-csrftoken":self.csrf,
				"X-Instagram-AJAX":"1",
				"X-Requested-With":"XMLHttpRequest",
				}
			r=_session.post(posturl,data=self.data,headers=header,verify=True)
			print(r)
		def create_ajax(self):
			self.passwd=user_list[0][1]
			self.u_name=user_list[0][0]
			r_data={
				'password': self.passwd,#密码
				'username':self.u_name,#账号（不能重复）
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
		def like(self):
			
    		
logintest=login()
logintest.do_first()