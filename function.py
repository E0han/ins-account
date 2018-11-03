#login and function
import account_info
import requests,re,json,time,os,os.path,sys
from data import header, name
from random import randint
from bs4 import BeautifulSoup
from proxy import proxy_pool
#数据
user_list=account_info.account
class functions():
		def __init__(self,proxy,session):
			self.proxy=proxy
			self._session=session
		def like(self):
			likeurl="https://www.instagram.com/web/likes/1781561095543136899/like/"
		def follow(self,userid):
			for i in userid:
				header['cookie']=str(self.read_cookies())[1:-2]
				header['X-csrftoken']=self.read_cookies()["csrftoken"]
				self.id=self.get_userid(i)
				header['refer']=self.user_profile
				followurl="https://www.instagram.com/web/friendships/"+self.id+"/follow/"
				r = self._session.post(followurl,headers=header,verify=True)
				print(r)
				#proxies=self.proxy
				if r.ok==True:
					print("[*] Sucessful follow the user",i)
					self._session.close()
				else:
					self._session.close()
					print("[x] Unknown Error Occurs!")
		def get_userid(self,userid):
			self.user_profile="https://www.instagram.com/"+str(userid)+'/'
			r = self._session.get(self.user_profile,verify=True)#proxies=self.proxy
			id=r.text.split('\",\"show_suggested_profiles')[0].split('profilePage_')[-1]
			return id
			
		def save_cookies(self):
			global _session
			with open('./'+"cookiefile",'w')as f:
				json.dump(self._session.cookies.get_dict(),f)#_session.cookies.save()
		def read_cookies(self):
			#_session.cookies.load()
			#_session.headers.update(header_data)
			with open('./'+'cookiefile')as f:
				cookie=json.load(f)
				self._session.cookies.update(cookie)
				return cookie