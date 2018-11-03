from function import functions
from register import register
from proxy import proxy_pool, get_one_from_pool
from login import login
import requests

ses=requests.session()
pool=proxy_pool(1)
proxy_use=get_one_from_pool(pool)
print(proxy_use)
logintest=login(proxy_use, [['test','test!']], ses)
logintest.run()
#fo=functions(proxy_use,ses)
#fo.follow(['judycin04'])