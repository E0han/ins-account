#Proxy Module for collecting proxy ip and put them into a pool
#__data__=='16/5/2018'
#utf-8
import requests
import json
url="http://gimmeproxy.com/api/getProxy"
s=requests.session()
def proxy_pool(amount_of_ip):
    pool={}
    print("[*] Get",str(amount_of_ip),"Annoymous IP Proxy")
    mainurl="https://gimmeproxy.com/api/getProxy?get=true&anonymityLevel=1&supportsHttps=True"
    for i in range(amount_of_ip):
        s=requests.session()
        r=s.get(mainurl,verify=True)
        r=json.loads(r.text)
        res='https://'+r['ipPort']
        if res not in pool.values():
            pool['https']=res
        else:
            print("[!] IP",r['ipPort'],"is already there")
            continue
    return pool
def test():
    ipPool=proxy_pool(1)
    print(ipPool)
    url='https://api.ipify.org?format=json'
    try:
        res=s.get(url,proxies=ipPool,verify=True)
        dic=json.loads(res.text)
        print(dic["ip"])
    except ProxyError:
        print("Can not connect to the ip proxy")
test()


