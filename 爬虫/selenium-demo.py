# _*_ coding:utf-8 _*_
# @time  : 2020/8/22 15:39
# @Author: quanwen
# @File  :
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
try:
    browser.get('http://www.taobao.com')
    first = browser.find_element_by_id('q')
    second = browser.find_element_by_css_selector('#q')
    thrid = browser.find_element_by_xpath('//*[@id="q"]')
    # input.send_keys(Keys.ENTER)
    print('查找元素： ',first,second,thrid)

    ''' 打印结果如下
    查找元素： 其中element的值表示这个元素的代号
    < selenium.webdriver.remote.webelement.WebElement(
        session="fae15a649f1fc19707aa6117fa02e401",element="b9148f7d-246d-4926-891a-e3eb62fa37e2") >
    < selenium.webdriver.remote.webelement.WebElement(
        session="fae15a649f1fc19707aa6117fa02e401",element="b9148f7d-246d-4926-891a-e3eb62fa37e2") >
    < selenium.webdriver.remote.webelement.WebElement(
        session="fae15a649f1fc19707aa6117fa02e401", element="b9148f7d-246d-4926-891a-e3eb62fa37e2") >
    '''

    lis = browser.find_elements_by_css_selector('.service-bd li')
    print('lis: ',lis)
    # wait = WebDriverWait(browser,10)
    # wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    # print('current_url: ',browser.current_url)
    # print('cookies: ',browser.get_cookies())
    # # 获取网页渲染后的源代码
    # print('page_source: ',browser.page_source)

    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_id('draggable')
    dis = browser.find_element_by_id('droppable')
    actions = ActionChains(browser)
    # 设置从哪拖拽到哪
    actions.drag_and_drop(source,dis)
    # 执行拖拽
    actions.perform()
    # time.sleep(2)
    # 切换到alert
    alert = browser.switch_to.alert
    # time.sleep(2)
    # 获取alert的文本
    print(alert.text)
    # 点击alert页面的确定
    alert.accept()
    time.sleep(5)
    browser.get('http://www.zhihu.com/explore')
    time.sleep(5)
    # 执行js
    # browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # browser.execute_script('alert("To Bottom")')
    ar = browser.find_element_by_css_selector('.Tabs-item--noMeta')

    print('attr: ',ar)
    # get_attribute('属性名') 获取元素的属性值
    print('attr: ',ar.get_attribute('innerText'))
except Exception:
    print('异常了？')
finally:
    pass
    # browser.close()