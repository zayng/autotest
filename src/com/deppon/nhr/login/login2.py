#-*- coding:utf-8 -*-
'''
Created on 2015年11月2日

@author: 119937
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from com.deppon.nhr import *

log=Logger()

def nhrLogin(self,user="231432",password="qqqqqq"):
    '初始化设置，实现NHR登陆，菜单选择'
    log.info("初始化设置，实现NHR登陆，菜单选择")
    self.driver=webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.url="http://192.168.68.125:8080/nhr/login/index.action"
    self.driver.get(self.url)
    log.info("logon nhr"+"username:"+user+" password:"+password)
    self.driver.find_element_by_id("loginName").send_keys(user)
    self.driver.find_element_by_id("password").send_keys(password)
    self.driver.find_element_by_class_name("a_login").click()
    self.driver.maximize_window()
    log.info("logon success!!!")
    print("NHR登陆成功")
        
def menu(self,s=2):
    driver=self.driver
    sleep(s)
    t1=driver.find_element_by_xpath(u"//div[text()='HR单据申请']").click()
    sleep(s)
    t2=driver.find_element_by_xpath(u"//div[text()='储备认证管理']").click()
    sleep(s)
    t3=driver.find_element_by_xpath(u"//div[text()='认证']").click()
    sleep(s)
    t4=driver.find_element_by_xpath(u"//div[text()='认证开班管理']").click()
    sleep(s+1)
    print("进入认证管理")
def logout(self):
    self.driver.quit()        
               
if __name__=="__main__":
    login=nhrLogin(nhrLogin)
    menu=menu(menu)
        

     