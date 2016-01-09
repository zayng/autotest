# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
import time

from selenium import webdriver

from com.deppon.hrpr.publ.log4 import Logger


class Page(object):
    """
    页面类基类，用于所有页面的继承。
    """

    base_url = 'http://192.168.20.116:8080/nhr/login/index.action'

    def __init__(self, base_url):
        self.url = base_url
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.log = Logger().get_log()
        self.sleep = time.sleep

    def open(self):
        self.log.info("启动FireFox浏览器，打开url.")
        self.driver.get(self.url)
        self.driver.maximize_window()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_element_by_xpath(self, loc):
        return self.driver.find_element_by_xpath(loc)

    def find_element_by_id(self, loc):
        return self.driver.find_element_by_id(loc)

    def find_element__by_class_name(self, loc):
        return self.find_element__by_class_name(loc)

    def find_element_by_name(self, loc):
        return self.driver.find_element_by_name(loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def find_elements_by_xpath(self, loc):
        return self.driver.find_elements_by_xpath(loc)

    def script(self, scr):
        self.driver.execute_script(scr)

# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     login = Page(driver)
#     login.uri = '/'
#     login.open()
