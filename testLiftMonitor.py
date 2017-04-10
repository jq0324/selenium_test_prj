# -*- coding: utf-8 -*-
import time
import datetime
import traceback
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def work(browser):
    url =  "http://192.168.20.105:9110/dt"
    browser.get(url)
    try:
        browser.find_element_by_name('username').send_keys('zhengqiang')
        
        browser.find_element_by_name('password').send_keys('admin' + Keys.ENTER)
        time.sleep(5)
        
        
        elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "电梯监控")))
        ActionChains(browser).move_to_element(elem).perform()
        
        elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "列表模式监控")))
        ActionChains(browser).click(elem).perform()
        
      
        time.sleep(5)
        try:
            browser.switch_to.frame("contentWrap")                  #into frame
            browser.find_element_by_id("liftName_s").send_keys('恋') #keyword for search
            time.sleep(1)
            browser.find_element_by_id("queryLiftButton").click()    #click search button 
            time.sleep(1)

            browser.find_element_by_css_selector(".scroll_table > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)").click()
            time.sleep(1)
            browser.find_element_by_css_selector("input.btn:nth-child(3)").click() #点击单梯监控 按键
            time.sleep(30)
            try:
                browser.find_element_by_css_selector("#basic-modal-content-1") # 确认打开单梯监控界面
                print("success to open oneLiftmonitor page")
            except:
                print("fail to open oneLiftMonitor page.........")
                writeLog()
                
            print("success to open liftControlInit page...")
        except:
            print("fail to open liftControlInit page...")
            writeLog()
            

    except:
        print ("failure")
        writeLog()
 

def writeLog():
    
    basename = os.path.splitext(os.path.basename(__file__))[0]
    logFile = basename+"-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".log"
    logging.basicConfig(filename=logFile)
    s = traceback.format_exc()
    logging.error(s)
    browser.get_screenshot_as_file("./"+logFile+"-screenshot_error.png")
 
if __name__ == "__main__":
    iedriver = "D:\selenium\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = iedriver
    browser = webdriver.Ie(iedriver)
    work(browser)
    browser.quit()
