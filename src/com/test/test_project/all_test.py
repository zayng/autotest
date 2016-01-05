from com.test.test_project import testadd,testsub1
import unittest
import os
def creatsuite():
    testunit=unittest.TestSuite()
    test_dir=os.path.abspath('.')
    print(test_dir)
    discover=unittest.defaultTestLoader.discover(test_dir, 'test*.py')
    return discover
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(creatsuite())