# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
browser = webdriver.Firefox()
'''
iedriver = "D:\selenium\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
browser = webdriver.Ie(iedriver)

browser.get('http://192.168.20.105:9110/dt/')
#assert 'Yahoo!' in browser.title

time.sleep (2)
browser.find_element_by_name('username').send_keys('zhengqiang')

browser.find_element_by_name('password').send_keys('admin' + Keys.RETURN)
time.sleep(5)

#elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"main_nav\"]/ul/li[2]/a")))

elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "设备管理")))
#  browser.find_element_by_link_text("设备管理") #browser.find_element_by_xpath("//*[@id=\"main_nav\"]/ul/li[2]/a")
ActionChains(browser).move_to_element(elem).perform()

elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "电梯资料管理")))
ActionChains(browser).click(elem).perform()

#browser.find_element_by_xpath("//*[@id=\"main_nav\"]/ul/li[2]/ul/li[1]/a").click()
time.sleep(2)
url = browser.current_url
print(url)
if url == "http://192.168.20.105:9110/dt/login/frameIndex.do":
    print("success")
else:
    print("failed")

time.sleep(15)

browser.quit()
