#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
import unittest
from com.test.test2 import is_prame

class testPrame(unittest.TestCase):
    def setUp(self):
        print('test start.')
    def test_zero(self):
        self.assertFalse(is_prame(0))
    def test_1(self):
        self.assertFalse(is_prame(1))
    def test_2(self):
        self.assertTrue(is_prame(2))
    def test_3(self):
        self.assertTrue(is_prame(3))
    def test_10(self):
        self.assertFalse(is_prame(10))
    def tearDown(self):
        print('test end.')
if __name__=='__main__':
    unittest.main()