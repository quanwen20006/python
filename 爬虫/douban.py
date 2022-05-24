# _*_ coding:utf-8 _*_
# @time  : 2020/8/17 15:28
# @Author: quanwen
# @File  :
import requests
import re
url = 'https://book.douban.com/'
cookies = {'cookie':'bid=K6iq8vN7XRg; gr_user_id=0333f9d9-17e9-42a9-8072-89a9aec0cef6; _vwo_uuid_v2=DF46F24070A14B7BE32E7227AF68D7708|1922a22d15114f20cc510f2e2f4f9876; __yadk_uid=twwVdSTPh7iP7XafpLnLrg0sW0UxUelc; __gads=ID=694f2569445f0131:T=1596590492:S=ALNI_MZ6NhXQknJXXNIng8V0Nq9pgbvuwQ; viewed="34879433"; __utmc=30149280; __utmz=30149280.1597066009.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=81379588; __utmz=81379588.1597066009.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=d8ca33e1-c907-41c6-9215-87891daaa362; gr_cs1_d8ca33e1-c907-41c6-9215-87891daaa362=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1597649423%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DD-siiemuvnllb4W4x5Zh4RS4-OlVKnA9apwcShlMoHxyF12UNgB1-wyCiy9xrDTrxGfFsitYos9vgoevmof_gq%26wd%3D%26eqid%3Dd9a3ac4e0012c987000000065f314b13%22%5D; _pk_id.100001.3ac3=f8659c22ad0e85cc.1596590489.3.1597649423.1597066008.; _pk_ses.100001.3ac3=*; ap_v=0,6.0; __utma=30149280.67244745.1596590492.1597066009.1597649423.3; __utmt_douban=1; __utmb=30149280.1.10.1597649423; __utma=81379588.1777879442.1596590492.1597066008.1597649423.3; __utmt=1; __utmb=81379588.1.10.1597649423; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_d8ca33e1-c907-41c6-9215-87891daaa362=true'}
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# content = requests.get(url,headers=headers,cookies=cookies).text
content = requests.get(url,headers=headers).text
# print('content: ', content)

#正则匹配
patt = re.compile('<li.*?cover.*?href="(.*?)"\s*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>', re.S)
# patt = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>', re.S)
result = re.findall(patt,content)
# print('results: ', result)
for item in result:
    url, title,author,year = item
    author = re.sub('\s','',author)
    year = re.sub('\s', '', year)
    print(url, title,author,year)
