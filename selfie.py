#get selfies from plxabay.com
#coding='utf-8'
#__author__=='0han'
#__email__=='0han@protonmail.com'
#__data__=='2017.8'
import requests
import json
import os
class selfie(object):
    def __init__(self):
        print("==Getting-selfies==")
        self.do()
    def do(self):
        self.key="6200454-44e39a368568209aa387741e5"
        self.s_url=s_url="https://pixabay.com/api/?key="+self.key+"&q="+"people"
        try:
            r=requests.get(self.s_url,verify=True)
            print(r.json)
        except requests.exceptions.SSLError:
            print("\n[x] SSL-Error!\n[!] Pls changing your network environment\n")
    def generate_payload(self):
        pass
    def download_pic(self):
        #input self.first_path & selfie_url
        path=os.mkdir("pic/"+self.first_path)
        pic_url=self.selfie_url
        down_pic=requests.get(pic_url,verify=True)
        with open(path+'/1.jpg',"wb") as file:
            file.write(down_pic.content)
    def delete_local_pic(self,path):
        os.remove(path)#path should looks like '/pic/selfie/1.jpg'

test=selfie()