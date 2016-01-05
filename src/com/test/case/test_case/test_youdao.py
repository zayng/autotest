from selenium import webdriver
import unittest,time

class test_youdao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.baseurl="http://www.youdao.com"
    def test_youdao(self):
        driver=self.driver
        driver.get(self.baseurl)
        driver.find_element_by_id("query").send_keys('selenium')
        driver.find_element_by_id("qb").click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title, "selenium - 有道搜索")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()