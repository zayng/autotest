#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


driver=webdriver.Firefox()
driver.get("http://192.168.20.21/bse-baseinfo-web/login/index.action")
def loginFoss():
    driver.implicitly_wait(5)
    username=driver.find_element_by_id("loginName")
    username.send_keys("084544")
    passwd=driver.find_element_by_id("password")
    passwd.send_keys("111111")
    login=driver.find_element_by_class_name("a_login").click()
    print("登录FOSS成功!!!")
def menuNav():
    driver.implicitly_wait(10)
    driver.maximize_window()
    sleep(2)
    mange=driver.find_element_by_xpath(u"//div[text()='装车管理']").click()
    
if __name__=='__main__':
    loginFoss()
    menuNav()  