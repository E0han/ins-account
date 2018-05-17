#register module
#coding='utf-8'
#__author__=='0han'
#__email__=='0han@protonmail.com'
#__data__=='17/5/2018'
import requests,re,json,time,os,os.path,sys
from data import header, name
from random import randint
from bs4 import BeautifulSoup
from proxy import proxy_pool

class register():
		def __init__(self):
			#ipproxy,num
			#self.proxy=self.get_one_from_pool(ipproxy,num)
			self._session=None
			print("==Instagram-robots-account-generate==\n[*] start")#可以删除 deletable
		def run(self):
			self._session=requests.session()
			self._session.get('https://www.instagram.com',verify=True)#proxies=self.proxy
			self.save_cookies()
			header['cookie']=str(self.read_cookies())[1:-2]
			header['X-csrftoken']=self.read_cookies()["csrftoken"]
			self.data=self.create_ajax()
			self.ins()
			time.sleep(5)
		def ins(self):
			global _session
			r = self._session.post('https://www.instagram.com/accounts/web_create_ajax/',data=self.data,headers=header,verify=True)#proxies=self.proxy
			if r.ok==True:
				print("[*] Sucessful create an account")
				self.save_account_info(self.u_name,self.passwd)
			else:
				print("[x] Unknown Error Occurs!")

		"""
			The method create_ajax(self) will return a ajax payload form which used to post to account creatation 
		"""
		def create_ajax(self):
			def get_emailaddress():
				r=requests.get("https://10minutemail.net",verify=True)
				r.encoding='utf-8'
				soup = BeautifulSoup(r.text, 'html.parser')
				return soup.input["value"]
			def generate_FullName():
				nameList=name['name']
				name=nameList[randint(1,12)]
				return name
			def create_username():
				data={'keyword':self.f_name,"numlines":"70","formsubmit":"Generate Username"}
				r=requests.post("http://namegenerators.org/username-generator/",data=data,verify=True)
				r.encoding='utf-8'
				soup=BeautifulSoup(r.text,'html.parser')
				result=soup.select(".section > div:nth-of-type("+str(randint(1,69))+")")[0].string
				result=str(result)+"no"+str(randint(1,20000))
				return result
			self.email=get_emailaddress()
			self.f_name=generate_FullName()
			self.passwd=self.f_name+'password'
			self.u_name=create_username()
			r_data={
				'email': self.email, #email for register
				'password': self.passwd,#password
				'username':self.u_name,#
				'first_name': self.f_name,#全名
				'seamless_login_enabled': 1,
				'tos_version': 'row'
				}
			return r_data
		def save_cookies(self):
			global _session
			with open('./'+"cookiefile",'w')as f:
				json.dump(self._session.cookies.get_dict(),f)#_session.cookies.save()
		def read_cookies(self):
			global _session
			#_session.cookies.load()
			#_session.headers.update(header_data)
			with open('./'+'cookiefile')as f:
				cookie=json.load(f)
				self._session.cookies.update(cookie)
				return cookie
		"""
			This internal function will get a random proxy ip from the pool which take as an argument
		"""
		def get_one_from_pool(self,pool,num):
			res={}
			ipPool = pool
			res['https']=ipPool[randint(0,num)]
			return res
		def save_account_info(self,username,password):
			with open("account_info.py", "a+") as a:
				a.write("\n['"+username+"','"+password+"'],")

#proxy=proxy_pool(10)
#print(proxy)
test=register()
test.run()
