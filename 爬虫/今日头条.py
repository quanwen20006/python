# _*_ coding:utf-8 _*_
# @time  : 2020/8/23 16:35
# @Author: quanwen
# @File  :
import json
import os
from hashlib import md5
from urllib import parse
import requests
from requests.exceptions import RequestException
import re
import mongo
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient(mongo.MONGO_URL)
db = client[mongo.MONGO_DB]

def get_page_index(offset,keyword):
    data ={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1
    }
    # urlencode 把字典转换为url请求参数
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search/?' + parse.urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page_index(html):
    # 把字符串转换为json对象
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    # print('详情页url： ',url)
    try:
        header= {
            'host': 'www.toutiao.com',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'content-type':'text/html; charset=utf-8'
        }
        cookies = {'cookie':'tt_webid=6864100026177570318; s_v_web_id=verify_ke6uug0g_G8QzhHF7_x9l2_4Lt6_8QZ8_w5bYT3HfD9pS; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6864100026177570318; csrftoken=826affe94339078742134a5da72a170d; ttcid=a026eb09be33425382dad3504410e23134; MONITOR_WEB_ID=9df2a84e-738b-430b-8f5f-4567974ed6a9; __tasessionId=0coppxoi41598186963418; __ac_nonce=05f4277260060ae7988c7; __ac_signature=_02B4Z6wo00f01eKjeOwAAIBDOJ5fOOzfBaHip3xAACft9mEoeuJz-wg7PDCFZcZz8VWJeaCyplNW8TWyyuzpSsRL2.TUxRALLU1mWIBbZ3Uc0mFI94Cd1czE3NoNIT2XiyUlhrjgRaIsHxRt7d; tt_scid=zhoX6IBUFo.OoFN6swirAs3UqjjO6.qjfp4hNY1L2md5xkK98fr39.IgoHwBpVUIbd34'}
        response = requests.get(url,headers=header,cookies=cookies)
        if response.status_code == 200:
            # print('response.text: ',response.text)
            return response.text
        return None
    except RequestException:
        print('请求详情页报错',url)
        return None

def parse_page_detail(html):
    pattern = re.compile('<!DOCTYPE html>.*?articleInfo.*?content: (\'.*?\')', re.S)
    list = re.findall(pattern, html)
    if list:
        pa = re.compile('.*?https:(.*?);pc', re.S)
        # print('list[0]: ',list[0])
        listTemp = re.findall(pa, list[0])
        # print('listTemp: ',listTemp)
        for item in listTemp:
            item = 'https:' + item
            new_url = item.replace('\\u002F','/')
            # print('解码: ', new_url)
            download_image(new_url)

def download_image(url):
    try:
        response = requests.get(url)
        # print('response.status_code: ',response.status_code)
        if response.status_code == 200:
            # response.content 返回二进制内容  response.text 文本内容
            save_image(response.content)
            return response.text
        return None
    except RequestException:
        print('请求图片错误', url)
        return None

def save_image(content):
    # 文件路径 文件名 文件后缀
    file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset,'街拍')
    for url in parse_page_index(html):
        if url:
            url = 'https://www.' + url[7:]
            html = get_page_detail(url)
            if html:
                parse_page_detail(html)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
    # main()