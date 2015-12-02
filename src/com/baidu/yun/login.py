#-*- coding:utf-8 -*-
'''
Created on 2015年11月30日

@author: sufy
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.get("http://yun.baidu.com/")
driver.implicitly_wait(30)
driver.maximize_window()
username=driver.find_element_by_name('userName')
username.clear()
username.send_keys('orcex')
password=driver.find_element_by_name('password')
password.send_keys('rh0h7cyi')

driver.find_element_by_id('TANGRAM__PSP_4__submit').click()

driver.find_element_by_xpath("//ul[@class='app-entry']/li[1]").click()

driver.refresh()

driver.find_element_by_xpath("//span[@title='nessus']").click()

ctreatfile=driver.find_element_by_xpath("//a[@class='icon-btn-createfile']")
ctreatfile.click()

creatname=driver.find_element_by_class_name("box")
creatname.send_keys(u'德邦物流有限公司')
driver.find_element_by_class_name("sure").click()

filename=driver.find_element_by_xpath("//span[text()='德邦物流有限公司']")
ActionChains(driver).context_click(filename).perform()

rename=driver.find_element_by_xpath("//@data-key='rename'")
rename.click()




