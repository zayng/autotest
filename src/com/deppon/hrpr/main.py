# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
import unittest

from com.deppon.hrpr.test_user_login import test_user_login
from selenium import webdriver


class Test126(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_login(self):
        username = 'suesce@126.com'
        password = '112200'
        test_user_login(self.driver, username, password)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
