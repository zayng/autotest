# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from selenium import webdriver
from com.deppon.hrpr.pages.login import LoginNHR
from com.deppon.hrpr.pages.queryclass import QueryClass
driver = webdriver.Firefox()
login = LoginNHR(driver)
login.user_login()
query = QueryClass()
query.queryclass_page(*(1, 1))

