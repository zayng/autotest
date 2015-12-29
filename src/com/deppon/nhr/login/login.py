#-*- coding:utf-8 -*-
'''
Created on 2015年11月2日

@author: 119937
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from com.deppon.nhr import log



class nhrLogin():
    '初始化设置，实现NHR登陆，菜单选择'
    def __init__(self):
        log.info("开始测试......")
        log.info("进行测试初始化工作")
        self.driver=webdriver.Firefox()
        self.url="http://192.168.68.125:8080/nhr/login/index.action"
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        log.info("初始化工作完毕")
        
    def login(self,user="231432",password="qqqqqq"):
        log.debug("打开系统链接:"+self.url)
        self.driver.get(self.url)
        log.debug("使用测试工号："+user)
        log.debug("测试密码："+password)
        self.driver.find_element_by_id("loginName").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("a_login").click()
        log.info("NHR login success!!!")
        
    def menu(self,s=2):
        driver=self.driver
        sleep(s)
        log.info("选择NHR菜单，HR单据申请-储备认证管理-认证-认证开班管理")
        driver.find_element_by_xpath(u"//div[text()='HR单据申请']").click()
        sleep(s)
        driver.find_element_by_xpath(u"//div[text()='储备认证管理']").click()
        sleep(s)
        driver.find_element_by_xpath(u"//div[text()='认证']").click()
        sleep(s)
        driver.find_element_by_xpath(u"//div[text()='认证开班管理']").click()
        sleep(s+1)
        log.info("进入认证管理")
        
    def logout(self):
        log.info("测试完成，退出浏览器。")
        self.driver.quit()        
     
    def EelementExits(self,value):
        try:
            self.driver.implicitly_wait(5)
            log.info("检查是否登录成功.")
            self.driver.find_element_by_xpath(value)
            self.driver.implicitly_wait(30)
            log.info("登录成功.")
            return True 
        except NoSuchElementException as r:
            log.info("登录失败")
            log.error(r)
            return False
        
                     
if __name__=="__main__":
    login=nhrLogin()
    login.login()
    login.menu()
    login.logout()
        

     