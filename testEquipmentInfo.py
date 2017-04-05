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
    url = "http://192.168.20.105:9110/dt"
    browser.get(url)
    try:
        browser.find_element_by_name('username').send_keys('zhengqiang')
        
        browser.find_element_by_name('password').send_keys('admin' + Keys.ENTER)
        time.sleep(5)
        
        #elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"main_nav\"]/ul/li[2]/a")))
        
        elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "设备管理")))
        #  browser.find_element_by_link_text("设备管理") #browser.find_element_by_xpath("//*[@id=\"main_nav\"]/ul/li[2]/a")
        ActionChains(browser).move_to_element(elem).perform()
        
        elem = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "设备资料管理")))
        ActionChains(browser).click(elem).perform()
        
        #browser.find_element_by_xpath("//*[@id=\"main_nav\"]/ul/li[2]/ul/li[1]/a").click()
        time.sleep(5)
        try:
            browser.switch_to.frame("contentWrap")
            browser.find_element_by_xpath("//*[@id=\"equipment_table-box\"]/div[2]/div/div[1]/table/thead/tr/th[1]")       
            print("success to open Equipmentinfo page...")
        except:
            print("fail to open Equipmentinfo page...")
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
