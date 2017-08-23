#get pictures from plxabay.com
#coding='utf-8'
#__author__=='0han'
#__email__=='0han@protonmail.com'
#__data__=='2017.8'
import requests
import json
import os
from random import randint
class get_pic(object):
    def __init__(self):
        self.key="6200454-44e39a368568209aa387741e5"
    def get_selfie(self):
        print("==Getting-selfie-pictures==")
        self.s_url=s_url="https://pixabay.com/api/?key="+self.key+"&q="+"people"
        try:
            r=requests.get(self.s_url,verify=True)
            dict_2 =json.loads(r.text)
            self.selfie_url=dict_2["hits"][randint(1,6)]["webformatURL"]
            self.download_pic("selfie")
        except requests.exceptions.SSLError:
            print("\n[x] SSL-Error!\n[!] Pls changing your network environment\n")

    def get_post_pic(self):
        print("==Getting-post-pictures==")
        self.s_url=s_url="https://pixabay.com/api/?key="+self.key+"&q="+"music"
        try:
            r=requests.get(self.s_url,verify=True)
            dict_2 =json.loads(r.text)
            self.selfie_url=dict_2["hits"][randint(1,6)]["webformatURL"]
            self.download_pic("PostPic")
        except requests.exceptions.SSLError:
            print("\n[x] SSL-Error!\n[!] Pls changing your network environment\n")

    def download_pic(self,first_path):
        #input first_path(selfie or post_pictures) & selfie_url
        if(os.path.exists(first_path)):
            print("[-] 打开"+first_path+"目录")
            
        else:
            path=os.mkdir(first_path)
        pic_url=self.selfie_url
        down_pic=requests.get(pic_url,verify=True)
        with open(first_path+'/1.jpg',"wb") as file:
            file.write(down_pic.content)
    def delete_local_pic(self,path):
        os.remove(path)#path should looks like '/selfie/1.jpg' 
