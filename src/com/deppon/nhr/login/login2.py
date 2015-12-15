#-*- coding:utf-8 -*-
'''
Created on 2015年11月2日

@author: 119937
'''
from time import sleep
import logging,os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def Logger1(name=os.path.join(os.getcwd(),'log1.txt'),clevel=logging.DEBUG,flevel=logging.DEBUG):
    logger=logging.getLogger('brunch')
    logger.setLevel(logging.DEBUG)
    fmt=logging.Formatter('[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')
    #日志从控制台输出
    sh=logging.StreamHandler()
    sh.setLevel(clevel)
    sh.setFormatter(fmt)
    #日志输出到文件
    fh=logging.FileHandler(name)
    fh.setLevel(flevel)
    fh.setFormatter(fmt)
    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger


class nhrtest():
    
    def __init__(self):
        '初始化设置，实现NHR登陆，菜单选择'
        global log
        log=Logger1()
        log.info("初始化设置，实现NHR登陆，菜单选择")
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.url="http://192.168.68.125:8080/nhr/login/index.action"
    def nhrLogin(self,user="231432",password="qqqqqq"):
        self.driver.get(self.url)
        log.info("logon nhr"+"username:"+user+" password:"+password)
        u=self.driver.find_element_by_id("loginName")
        u.clear()
        u.send_keys(user)
        p=self.driver.find_element_by_id("password")
        p.clear()
        p.send_keys(password)
        log.info("点击登录按钮")
        self.driver.find_element_by_xpath("//a[@class='a_login']").click()
        log.info("点击登录按钮完毕")
        sleep(3)
        
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
        log.info("打开认证管理界面")
        driver.find_element_by_xpath(u"//div[text()='认证开班管理']").click()
        sleep(s+1)
    
    def logout(self):
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
    #             log.info(r)
                return False              
if __name__=="__main__":
    t=nhrtest()
    with open("shadow.txt") as filename:
        for line in filename:
            user,pw=line.strip().split(",")
            t.nhrLogin(user, pw)
            log.info("调用EelementExits函数，校验NHR是否登录成功")
            f=t.EelementExits("//div[@id='footerPanel-innerCt']")
            if f:
                log.info("登录成功，进入NHR欢迎界面")
                break
            else :
                log.info("重新读取账号和密码登录。")
                continue
        else:
            t.logout()
        t.menu()
    t.logout()   
        

     