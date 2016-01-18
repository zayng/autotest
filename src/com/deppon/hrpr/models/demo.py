# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from selenium import webdriver
from com.deppon.hrpr.pages.login import LoginNHR
from com.deppon.hrpr.pages.newclass import AddClassName

driver = webdriver.Firefox()
login = LoginNHR(driver)
login.user_login()
auth = AddClassName(driver)
for large in range(13):
    for level in range(4):
        auth.classname_page(large, level)
        print("已经增加班级总数：", large * level)
