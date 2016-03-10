# -*- coding:utf-8 -*-
"""
Created on '2016/1/21'

@author: '119937'
"""
import unittest
import time
import os

from selenium import webdriver

from com.deppon.hrpr.models import HTMLTestRunner3
from com.deppon.hrpr.pages.login import LoginNHR
from com.deppon.hrpr.pages.newclass import AddClassName

class NewclassTest(unittest.TestCase):

    def login_nhr(self):
        login = LoginNHR(self.driver)
        login.user_login()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_nhr(self)

    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.login_nhr()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_add_classname_empty(self):
        """输入班级名称为空检验"""
        add = AddClassName(self.driver)
        add.add_newclass_page(classname='')
        self.assertTrue(add.is_element_present_required(), "必输项为空检验失败!")

    def test_add_classaddr_empty(self):
        """输入班级地点为空检验"""
        add = AddClassName(self.driver)
        add.add_newclass_page(classaddr='')
        self.assertTrue(add.is_element_present_required(), "必输项为空检验失败!")

    def test_add_middle_grade(self):
        """新增中级认证级开班"""
        add = AddClassName(self.driver)
        add.add_newclass_page()
        self.assertTrue(add.is_element_present_success(), "新增班级失败！")

    def test_add_high_grade(self):
        """新增高级认证级开班"""
        add = AddClassName(self.driver)
        add.add_newclass_page(large=0, level=1)
        self.assertTrue(add.is_element_present_success(), "新增班级失败！")

    def test_add_senior_grade(self):
        """新增高级认证开班"""
        add = AddClassName(self.driver)
        add.add_newclass_page(large=0, level=2)
        self.assertTrue(add.is_element_present_success(), "新增班级失败！")

    def test_add_expert_grade(self):
        """新增资深班级开班"""
        add = AddClassName(self.driver)
        add.add_newclass_page(large=0, level=3)
        self.assertTrue(add.is_element_present_success(), "新增班级失败！")

    def test_add_business(self):
        """新增所有认证开班"""
        add = AddClassName(self.driver)
        for la in range(13):
            for le in range(4):
                add.add_newclass_page(large=la, level=le)
                self.assertTrue(add.is_element_present_success(), "新增班级失败！")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NewclassTest("test_add_classname_empty"))
    suite.addTest(NewclassTest("test_add_classaddr_empty"))
    suite.addTest(NewclassTest("test_add_middle_grade"))
    suite.addTest(NewclassTest("test_add_high_grade"))
    suite.addTest(NewclassTest("test_add_senior_grade"))
    suite.addTest(NewclassTest("test_add_expert_grade"))
    suite.addTest(NewclassTest("test_add_business"))

    reportfile = 'result.html'
    with open(os.path.join(os.path.abspath('../log'), reportfile), 'wb') as rfile:
        runner = HTMLTestRunner3.HTMLTestRunner(stream=rfile,
                                                title="NHR-选拔认证管理测试报告",
                                                description="用例执行情况：")
        runner.run(suite)



