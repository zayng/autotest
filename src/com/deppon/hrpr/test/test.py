# -*- coding:utf-8 -*-
"""
Created on '2016/1/15'

@author: '119937'
"""

from com.deppon.hrpr.page.login import LoginNHR
from com.deppon.hrpr.page.authcla import AddClassName
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    login = LoginNHR(driver)
    login.opennhr()
    login.login()
    login.nav_menu()
    driver = login.driver
    ath = AddClassName(driver)
    ath.add_claname()
