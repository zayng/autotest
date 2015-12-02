#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
from com.test.count import count
import unittest

class test(unittest.TestCase):
    def setup(self):
        self.j=count(2,3)
    def test_add(self):
        self.add=self.j.add()
        self.assertEqual(self.add,5)
    def tearDown(self):
        pass
if __name__=='__main__':
    