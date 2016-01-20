# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
import time
import logging
import os

from selenium import webdriver
from com.deppon.hrpr.publ.log4g import logger1


class Page(object):
    """
    页面类基类，用于所有页面的继承。
    """

    login_url = 'http://192.168.20.116:8080/nhr/login/index.action'

    def __init__(self, base_driver=None, base_url=login_url):
        self.base_url = base_url
        self.driver = base_driver
        self.driver.implicitly_wait(30)
        self.log = logger1()

    def open(self):
        self.log.info("启动FireFox浏览器，打开url.")
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def findelement(self, *loc):
        return self.driver.find_element(*loc)

    def findelement_xpath(self, loc):
        return self.driver.find_element_by_xpath(loc)

    def findelement_id(self, loc):
        return self.driver.find_element_by_id(loc)

    def findelement_class_name(self, loc):
        return self.driver.find_elements_by_class_name(loc)

    def findelement_name(self, loc):
        return self.driver.find_element_by_name(loc)

    def findelements(self, *loc):
        return self.driver.find_elements(*loc)

    def findelements_xpath(self, loc):
        return self.driver.find_elements_by_xpath(loc)

    def script(self, scr):
        self.driver.execute_script(scr)

    @staticmethod
    def sleep(s):
        return time.sleep(s)

class Logger(object):

    def __init__(self, name=os.path.join(os.path.abspath('../log'), 'log.txt'), clevel=logging.DEBUG,
               flevel=logging.DEBUG):
        self.log4 = logging.getLogger('master')
        self.log4.setLevel(logging.DEBUG)
        fmat = "[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        fmt = logging.Formatter(fmat, '%Y-%m-%d %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)
        fh = logging.FileHandler(name)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        self.log4.addHandler(sh)
        self.log4.addHandler(fh)

    def get_log(self):
        return self.log4












    @staticmethod
    def logger(name=os.path.join(os.path.abspath('../log'), 'log.txt'), clevel=logging.DEBUG,
               flevel=logging.DEBUG):
        log4 = logging.getLogger('brunch')
        log4.setLevel(logging.DEBUG)
        fmat = "[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        fmt = logging.Formatter(fmat, '%Y-%m-%d %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setLevel(clevel)
        sh.setFormatter(fmt)
        fh = logging.FileHandler(name)
        fh.setLevel(flevel)
        fh.setFormatter(fmt)
        log4.addHandler(sh)
        log4.addHandler(fh)
        return log4
