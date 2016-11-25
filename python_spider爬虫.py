#coding:gbk

import urllib,urllib2

'''
response = urllib2.urlopen("https://www.baidu.com")
print response.read()
'''
'''
request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print response.read()
'''
#模拟登陆

'''
values = {"username":"1016903103@qq.com","password":"XXXX"}
cookie = 
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
'''
import re
url = "http://www.qiushibaike.com/"
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
#cookie = '_qqq_uuid_="2|1:0|10:1472369976|10:_qqq_uuid_|56:YzQ3MGY5Y2Y0ZGRjYTc5M2I5YzMyMTYzNjgxYzc3Nzg2ODZmNTQ5Yw==|f067df66b189548c04abc81f670f4e48b8efcdb34f825b94f24d06ad6288aa06"; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1472541808,1472631399,1472631432,1472631624; _ga=GA1.2.2134370680.1472369981; __cur_art_index=300; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1472631624'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url)
response = urllib2.urlopen(request)
con = response.read()


a = re.findall(r'<div class="content">(.*?)</div>',con,re.S)
f = open('10.txt','w')
for i in a:
    i.replace('<br/>','\n')
    #print i
    f.write(i)
f.close()
