#-*- coding:utf-8 -*-
'''
Created on 2015年11月6日

@author: 119937
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Ie()
url='http://hr.deppon.com:9080/eos-default/dip.integrateorg.oaAttence.oaAttence.flow'
driver.get(url)
driver.maximize_window()
user=driver.find_element_by_xpath("//input[@id='name']")
user.clear()
user.send_keys('119937')
passwd=driver.find_element_by_xpath("//input[@id='password']")
passwd.send_keys('852528zy')

img=driver.find_element_by_xpath("//img[@name='login_bg']")
img.click()

induty=driver.find_element_by_xpath("//div[@class]/a[1]")
induty.click()

