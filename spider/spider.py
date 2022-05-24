from urllib import request
import re
import ssl


class Spider(object):
    '''
    这个是一个类
    '''
    url = 'https://www.panda.tv/cate/lol'
    # 加问是去掉贪婪模式
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '<span class="video-nickname" [\s\S]*?></i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number"><i [\s\S]*?></i>([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url, context=ssl.SSLContext())
        htmls = r.read()
        # 把字节码转换为字符串
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        info = []
        root_html = re.findall(Spider.root_pattern, htmls)

        for html in root_html:
            # 去除原始数据的开始和结束空格
            name = re.findall(Spider.name_pattern, html)[0].strip()
            number = re.findall(Spider.number_pattern, html)[0]
            tempDict = {'name': name, 'number': number}
            info.append(tempDict)

        return info

    def __sort(self, infos):
        infos = sorted(infos, key=self.__sort_seed, reverse=True)
        return infos

    def __sort_seed(self, infomation):
        # 提取数据里面的数字
        number = float(re.findall('\d*', infomation['number'])[0])
        # 过万数量的-需要特殊处理
        if '万' in infomation['number']:
            number = float(re.findall('[\d+\.\d]*', infomation['number'])[0])
            number *= 10000
        print(number)
        return number

    def __show(self, infos):
        for i in range(len(infos)):
            print('排名: '+str(i+1)+'  昵称：'+infos[i]['name']+'  人数：'+infos[i]['number'])

    def go(self):
        htmls = self.__fetch_content()
        htmls = self.__analysis(htmls)
        htmls = self.__sort(htmls)
        self.__show(htmls)


if __name__ == '__main__':
    spider = Spider()
    spider.go()
