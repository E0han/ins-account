#Proxy Module for collecting proxy ip and put them into a pool
#__data__=='16/5/2018'
#utf-8
import requests
import json
from random import randint
"""
    The function proxy_pool is going to take an argument which indicates the amount 
    of the ip proxy addresses you want to have in the pool and return a list that contains
    ip proxyies without overloop.
"""
def proxy_pool(amount_of_ip):
    pool=[]
    print("[*] Get",str(amount_of_ip),"Annoymous IP Proxy")
    mainurl="https://gimmeproxy.com/api/getProxy?get=true&anonymityLevel=1&supportsHttps=True"
    for i in range(amount_of_ip):
        s=requests.session()
        r=json.loads(s.get(mainurl,verify=True).text)
        res='https://'+r['ipPort']
        s.close()
        if res not in pool:
            pool.append(res)
        else:
            print("[!] IP proxy address ",r['ipPort'],"is already in the pool")
            continue
    return pool # pool here is a list contains n's (the amount you indicate) ip in the form like "https://80.211.184.190:8888"
"""
    The test function is used to get a random ip from the pool and test whether it useable
    测试模块，在项目中可参看内置函数return_random_ipproxy的用法，从pool代理池中随机提取一个作为代理ip
"""
def test():
    def return_random_ipproxy(pool,num):
        res={}
        ipPool = pool
        res['https']=ipPool[randint(0,num)]
        return res
    ipPool=return_random_ipproxy(proxy_pool(5),5)
    print(ipPool)
    urlforlocalip='https://api.ipify.org?format=json'
    s=requests.session()
    try:
        res=s.get(urlforlocalip,proxies=ipPool,verify=True)
        dic=json.loads(res.text)
        print("[+] Your local ip address is",dic["ip"])
    except ProxyError:
        print("Can not connect to the ip proxy")
test()