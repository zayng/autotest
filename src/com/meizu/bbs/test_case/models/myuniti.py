# -*- coding:utf-8 -*-
"""
Created on '2016/1/11'

@author: '119937'
"""
import unittest
import os
from selenium import webdriver
from .driver import browser

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()