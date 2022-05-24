# _*_ coding:utf-8 _*_
# @time  : 2020/8/24 18:03
# @Author: quanwen
# @File  :
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
def search():
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys('美食')
        submit.click()
        # 删除cookie
        browser.delete_all_cookies()
        time.sleep(2)
        login_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fm-login-id")))
        login_user.clear()
        login_user.send_keys('quan4wen')
        login_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fm-login-password")))

        login_pwd.clear()
        login_pwd.send_keys('quanwen@#')

        login_scroll = browser.find_element_by_css_selector("#nc_1_n1z")
        # 拖动元素，x的轴距离，y轴的距离
        browser.maximize_window()
        b = ActionChains(browser)
        b.click_and_hold(on_element=login_scroll).perform()
        for i in range(100):
            try:
                b.move_to_element_with_offset(to_element=login_scroll, xoffset=90, yoffset=i).perform()
                # 登录失败的错误提示信息
                if browser.find_element_by_css_selector('#login-error > div'):
                    continue
            except Exception:
                break
        # b.reset_actions()

        time.sleep(1)


        # ActionChains(browser).click_and_hold(on_element=login_scroll).perform()
        # ActionChains(browser).move_to_element_with_offset(to_element=login_scroll, xoffset=40, yoffset=5).perform()
        # time.sleep(0.1)
        # ActionChains(browser).move_to_element_with_offset(to_element=login_scroll, xoffset=200, yoffset=10).perform()
        # time.sleep(0.1)
        # ActionChains(browser).move_to_element_with_offset(to_element=login_scroll, xoffset=300, yoffset=15).perform()
        # time.sleep(0.1)
        # ActionChains(browser).move_to_element_with_offset(to_element=login_scroll, xoffset=500, yoffset=20).perform()
        # time.sleep(0.1)
        # ActionChains(browser).move_to_element(login_scroll).release()

        login_btn = browser.find_element_by_css_selector('#login-form > div.fm-btn > button')
        login_btn.click()

        # total =
    except TimeoutException:
        print('异常了。。。。')
        # return search()

def main():
    search()

if __name__ == '__main__':
    main()