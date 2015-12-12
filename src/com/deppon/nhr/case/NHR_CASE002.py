from time import sleep
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from com.deppon.nhr import *
    
    
class Test002(unittest.TestCase):
    def setUp(self):
        log.info("开始执行测试用例")
        
    def test_login(self):
        try:
            startup(self)
            login(self)
        except Exception as e:
            log.error("执行测试异常"+e)
            return False        
           
    def tearDown(self):
        self.driver.quit()
        log.info("测试用例执行完毕")
if __name__=='__main__':
    unittest.main() 