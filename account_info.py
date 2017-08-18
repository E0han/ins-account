#emailadress:password
"""dic={
"wangjianyu1998@gmail.com":"wangjianyu"
"zpz05720@kyois.com":"zpz05720"
"dcf79904@kyois.com":"dcf79904"
"dsjfakj@djs.com":"woshijiqiren"
}"""
def savedata(email,passwd):
	dic[email]=passwd
	with open('account_info.txt','a') as f:
		f.write(email+':'+passwd+'\n')

