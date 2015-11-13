#-*- coding:utf-8 -*-
'''
Created on 2015年10月15日

@author: 119937
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class nhrtest():
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        
    def logon(self):
        driver=self.driver
#         print unicode(driver.current_url())
        driver.get("http://192.168.68.125:8080/nhr/login/index.action")
        self.assertIn(u"HR自助",driver.title())
        elem=driver.find_element_by_name("username")
        elem.click()
        elem.send_keys("119937")
        elempw=driver.find_element_by_name("password")
        elempw.click()
        elempw.send_keys("qqqqqq")
        elempw.send_keys(Keys.RETURN)
        assert u"您好，欢迎使用HR自助系统！" in driver.page_source()
        driver.save_screenshot("D:\screenshot.png")
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
     nhrt=nhrtest()
     nhrt.setUp() 
     nhrt.logon()
     nhrt.tearDown()