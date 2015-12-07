#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        number=int(input('please input number:'))
        self.number=number
    def test_case(self):
        self.assertEqual(self.number, 10, 'you are input 10')
    def tearDown(self):
        pass
    
if __name__=='__main__':
    unittest.main()