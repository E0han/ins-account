#login and function
import requests,re,json,time,os,os.path,sys
from random import *
import dic


#数据
class login():
		_session=None

		def __init__(self, u_name, passwd):
			self.u_name = u_name
			self.passwd = passwd
			pass
		def do_first(self):
			print("[*] Manage to login")
			global _session
			_session=requests.session()
			main_url='https://www.instagram.com'
			_session.get(main_url,verify=True)
			self.save_cookies()
			if os.path.exists('cookiefile'):#print('have cookies')
				self.csrf=self.read_cookies()
				self.data=self.create_ajax()
				return True if self.login_now() else False
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
			if r.status_code != 200:
				print('[x] Invalid Account! Insta +1 status_code=' + str(r.status_code))
				return False
			else:
				print('[*] Successfully login! Account Verified! status_code=' + str(r.status_code))
				return True

		def create_ajax(self):
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

			

#logintest=login('Lucasitkohauser1048', 'Lucaspassword')
# logintest=login('Lucasominfouser467', 'Lucaspassword')
# logintest.do_first()