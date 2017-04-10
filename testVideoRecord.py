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
        
        elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "视频录制记录")))
        ActionChains(browser).click(elem).perform()
        
      
        time.sleep(5)
        try:
            browser.switch_to.frame("contentWrap")                  #into frame
            browser.find_element_by_id("regiName_s").click()  #  小区选择
            time.sleep(3)
            browser.find_element_by_id("treeModalInput").send_keys("恋")
            #elem = WebDriverWait(browser,10).until(EC.visibility_of_element_located(By.CSS_SELECTOR,"#sObjLiunit_17"))
            #elem.click()
            time.sleep(1)
            browser.find_element_by_id("sObjLiunit_17").click() # 
            time.sleep(1)
            browser.find_element_by_css_selector("button.ui-button:nth-child(1)").click()# 确定按键
            time.sleep(2)
            browser.find_element_by_xpath("//*[@id=\"queryDtjkVideorecordeButton\"]").click()    #click search button 
            time.sleep(1)

            browser.find_element_by_css_selector(".scroll_table > tbody:nth-child(1) > tr:nth-child(2)").click()
            time.sleep(1)
            browser.find_element_by_css_selector("input.btn:nth-child(3)").click() #点击查看视频 按键
            time.sleep(30)
            try:
                browser.find_element_by_css_selector("#basic-modal-content-2") # 确认打开视频播放界面
                print("success to watch Record video page")
            except:
                print("success to watch Record video page.........")
                writeLog()
                
            print("success to open videoRecord page...")
        except:
            print("fail to open videoRecord page...")
            writeLog()
            

    except:
        print ("failure")
        writeLog()
 

def writeLog():
    
    basename = os.path.splitext(os.path.basename(__file__))[0]
    logFile = basename+"-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".log"
    logging.basicConfig(filename = "./log/" + logFile)
    s = traceback.format_exc()
    logging.error(s)
    browser.get_screenshot_as_file("./log/"+logFile+"-screenshot_error.png")
 
if __name__ == "__main__":
    iedriver = "D:\selenium\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = iedriver
    browser = webdriver.Ie(iedriver)
    work(browser)
    browser.quit()
