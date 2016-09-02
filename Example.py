#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
# -*- coding: gb2312 -*-

import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def myCheck():
    reload( sys )
    sys.setdefaultencoding('utf-8')
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.szjzz.gov.cn/index/queryResident")
    if (True):
        str = "chinese"
        str = unicode(str, errors='replace')
        elem = driver.find_element_by_id("name") 
        elem.send_keys(str)
        elem = driver.find_element_by_id("credentialsType")
        elem.find_element_by_xpath("//option[@value='1']").click()
        elem = driver.find_element_by_id("credentialsNum") 
        elem.send_keys("123456")
        elem = driver.find_element_by_id("ResiSubmit") 
        elem.click()
        time.sleep(1)
        driver.close()
        driver.quit()
    else:
        print("that is fine!")

def Main():
   myCheck()

if __name__ == "__main__":
    Main()
    print '\n--------------- all Over -----------------\n'
