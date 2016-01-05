from com.test.test_project.count import count
import unittest

class TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def test_sub(self):
        self.j=count(6,2)
        return self.assertEqual(self.j.sub(), 4)
    def test_sub1(self):
        self.j=count(6.4,3.7)
        return self.assertEqual(self.j.sub(), 2.7)
    def tearDown(self):
        pass
if __name__=='__mian__':
    unittest.main()