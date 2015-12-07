#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
import unittest
class test3(unittest.TestCase):
    def setUp(self):
        pass
    def test_case(self):
        self.a='hello'
        self.b='hello world'
        self.assertIsNot(self.a, self.b,msg='a is not b')
    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()