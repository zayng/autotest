from com.test.test_project import testadd,testsub1
import unittest

suite=unittest.TestSuite()
suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testadd.TestAdd("test_add3"))

suite.addTest(testsub1.TestSub("test_sub"))
suite.addTest(testsub1.TestSub("test_sub1"))
if __name__=='__mian__':
    runner=unittest.TextTestRunner()
    runner.run(suite)
