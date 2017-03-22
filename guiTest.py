# -*- coding: UTF-8 -*-
from pywinauto import Application
import time
import random


def getTime():
    return time.ctime(time.time())
    
def writeLogFile(num):
    curTime = getTime()
    f = open("num_exe.txt","a+")
    tmp = curTime + "  testNum: "+ str(num) + " start \n"
    f.write(tmp)
    f.close()
    


num = 1
app = Application(backend='win32').start("E:\\ZLPlaySDKTest\\PlaySDKTest.exe")
app.PlaySDKTest.Edit.TypeKeys("rtsp://192.168.20.63:55400/Stream/channel=1?sub_stream")
while 1: 
    writeLogFile(num)
    print (" Test %s start " %num)   
    num += 1 
    time.sleep(3)
    app.PlaySDKTest.Play.Click()
    sleepTime = random.randrange(30, 120, 1)
       
    print (" wait %s seconds"%(sleepTime))
    time.sleep(sleepTime)
    
    app.PlaySDKTest.Stop.Click()
    time.sleep (10)
    print(" test finish")
    
    time.sleep(3)



