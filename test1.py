from selenium import webdriver
import time
import os
import random

def getTime():
    return time.ctime(time.time())
    
def writeLogFile(num):
    curTime = getTime()
    f = open("hk_test.log","a+")
    tmp = curTime + "  testNum: "+ str(num) + " start \n"
    print(tmp)
    f.write(tmp)
    f.close()

def ieBrower():
    iedriver = "D:\selenium\IEDriverServer.exe"
    os.environ["webdriver.ie.driver"] = iedriver
    browser = webdriver.Ie(iedriver)
    return browser 


def start_autoTest():
    browser = ieBrower()
    browser.get('e:\\monitorSamplehk.html')
    assert 'Montitor' in browser.title
    num = 1
    while 1:   
        writeLogFile(num)
        #print (" Test %s start " %num)
        num += 1
        time.sleep (2)
        browser.find_element_by_xpath("//button[4]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//button[4]").click()
        time.sleep(1)
        
        browser.find_element_by_xpath("//button[3]").click()
        time.sleep(1)
     #   browser.find_element_by_xpath("//button[3]").click()
        sleepTime = random.randrange(30, 120, 1)
        
        print ("wait %s seconds"%(sleepTime))
        time.sleep(sleepTime)
        for i in range(1,4):
            browser.find_element_by_xpath("//button[5]").click()
            time.sleep(1)
        
        time.sleep (10)
        print("test finish")
         
    browser.quit()
    
    
start_autoTest()

    
    
