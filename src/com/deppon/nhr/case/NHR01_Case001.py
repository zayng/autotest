import unittest
import os


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from time import sleep
from com.deppon.nhr import Logger

global log
log=Logger()

def startup(self):
    log.info("。。。。。。初始化设置。。。。。")
    self.driver=webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()
    self.url="http://192.168.68.125:8080/nhr/login/index.action"

def login(self,user="231432",password="qqqqqq"):
    log.info("启动FireFox浏览器，打开url.")
    self.driver.get(self.url)
    log.info("使用账号登陆NHR系统")
    log.info("登陆账号:"+user)
    log.info("登陆密码:"+password)
    self.driver.find_element_by_id("loginName").send_keys(user)
    self.driver.find_element_by_id("password").send_keys(password)
    self.driver.find_element_by_class_name("a_login").click()

def menu(self,s=2):
    log.info("选择菜单节点")
    driver=self.driver
    sleep(s)
    t1=driver.find_element_by_xpath(u"//div[text()='HR单据申请']").click()
    sleep(s)
    t2=driver.find_element_by_xpath(u"//div[text()='储备认证管理']").click()
    sleep(s)
    t3=driver.find_element_by_xpath(u"//div[text()='认证']").click()
    sleep(s)
    t4=driver.find_element_by_xpath(u"//div[text()='认证开班管理']").click()
    sleep(s+1)
    
    
class Test001(unittest.TestCase):
    
    def setUp(self):
        log.info("开始执行测试用例")
        self.boolean=True
        
    def test_login(self):
        try:
            startup(self)
            login(self)
        except Exception as e:
            log.error("执行测试异常"+e)
            return False
        self.assertTrue(self.driver.find_element_by_tag_name("mainAreaPanel"))
#     def test_menu(self):
#         try:
#             log.info("打开导航")
#             menu(self)
#         except Exception as e:
#             self.boolean=False
#             log.error("执行测试异常"+e)
           
    def tearDown(self):
        self.driver.quit()
        log.info("测试用例执行完毕")
if __name__=='__main__':
    unittest.main()    