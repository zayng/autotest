from selenium import webdriver
import unittest,time

class test_baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.baseurl="http://www.baidu.com"
    def test_baidu(self):
        driver=self.driver
        driver.get(self.baseurl)
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        title=driver.title
        self.assertEqual(title, "selenium_百度搜索")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()