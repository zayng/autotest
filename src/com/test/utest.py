#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
from com.test.count import count
import unittest

class test(unittest.TestCase):
    def setUp(self):
        print('befor case')
        self.j=count(2,3)
    def test_add(self):
        self.add=self.j.add()
        self.assertEqual(self.add,5)
    def tearDown(self):
        print('after case')
if __name__=='__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(test("test_add"))
    
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run()
    