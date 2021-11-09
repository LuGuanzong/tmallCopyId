from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 利用终端打开浏览器
def open_browser():
    import os

    prefix = input('请输入目标浏览器位置：')
    # C:\Users\zjdell\AppData\Local\Google\Chrome\Application\chrome.exe
    path = prefix + r' --remote-debugging-port=9222 --user-data-dir=""'
    try:
        os.popen(path)
    except:
        print('注意：打开浏览器时出现错误！')
    sleep(0.05)


# 直接打开登录页面
def open_login_page(driver):
    driver.get('https://www.taobao.com/')
    sleep(0.05)
    try:
        if driver.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'):
            login_button = driver.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
            login_button.click()
    except:
        print(f'注意：无法正常打开登录页.')


# 接管准备好的谷歌浏览器
def takeover_browser():
    s = Service(r'static/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options = Options()
    try:
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    except:
        print("注意：接管浏览器时出现错误！")
    driver = webdriver.Chrome(service=s, options=options, chrome_options=chrome_options)
    open_login_page(driver)
    # assert len(driver.window_handles) == 1, '请保证当前谷歌浏览器只有一个页面'
    return driver


# 获取目标身份证号
def get_id(driver, order_id):
    origin_link = 'https://certify.tmall.hk/idcard/info.htm?id='
    link = origin_link + order_id
    driver.get(link)
    sleep(0.02)
    try:
        if driver.find_element(By.XPATH, '//*[@id="id-card"]/div[2]/table/tbody/tr[3]/td[2]'):
            id_number = driver.find_element(By.XPATH, '//*[@id="id-card"]/div[2]/table/tbody/tr[3]/td[2]')
            return id_number.text
    except:
        print(f'注意：无法找到订单号为"{order_id}"的订单所属客户身份证号.')
    return 0
