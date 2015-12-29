"""
Created on '2015/12/29'

@author: '119937'
"""

import unittest
from com.test.untest.prame import is_prime

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Startting test.")

    def test_prame7(self):

        self.assertTrue(is_prime(7), msg="It's not Prime numbers")
        print("Prime numbers")

    def test_prame8(self):

        self.assertTrue(is_prime(8), msg="It's not Prime numbers")
        print("Prime numbers1")
    def test_prame9(self):

        self.assertTrue(is_prime(9), msg="It's not Prime numbers")
        print("Prime numbers2")

    def test_prame10(self):
        self.assertTrue(is_prime(10), msg="It's not Prime numbers")
        print("Prime numbers3")

    def tearDown(self):
        print("test end.")

if __name__ == '__main__':
    unittest.main()
