# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from selenium import webdriver
from com.deppon.hrpr.page.login import LoginNHR
from com.deppon.hrpr.page.queryclass import QueryClass
driver = webdriver.Firefox()
login = LoginNHR(driver)
login.user_login()

