from com.test.test_project.count import count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_add(self):
        self.j=count(2,4)
        return self.assertEqual(self.j.add(), 6)
    def test_add2(self):
        self.j=count(2.4,3.7)
        return self.assertEqual(self.j.add(), 6.1)
    def test_add3(self):
        self.j=count('hello',' world')
        return self.assertEqual(self.j.add(), 'hello world')
    def tearDown(self):
        pass
if __name__=='__mian__':
    unittest.main()