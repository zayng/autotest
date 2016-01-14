# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
from com.deppon.hrpr.page.page import Page


class Login126(Page):
    """
    登录www.126.com页面
    """

    def opennhr(self):
        self.open()

    def login(self, user="231432", pwd="qqqqqq"):
        self.log.info("使用账号登陆NHR系统")
        self.log.info(user + ',' + pwd)
        username = self.driver.find_element_by_id("loginName")
        password = self.driver.find_element_by_id("password")
        loginbtn = self.driver.find_element_by_class_name("a_login")
        username.send_keys(user)
        password.send_keys(pwd)
        loginbtn.click()

    def nav_menu(self):
        self.log.info("开始打开NHR菜单节点：HR单据申请-储备认证管理-认证管理-认证开班管理。")
        nav_dat = ['储备认证管理', '认证管理', '认证开班管理']
        self.driver.find_element_by_xpath("//div[text()='储备认证管理']").click()
        self.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='认证管理']").click()
        self.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='认证开班管理']").click()
        # dat = nav_dat
        # for value in dat:
        #     self.driver.find_element_by_xpath("//div[text()='%s']" % value).click()
        #     self.sleep(3)

    @staticmethod
    def nav_dat():
        dat = ['储备认证管理', '认证管理', '认证开班管理']
        return dat

if __name__ == '__main__':
    login = Login126()
    login.opennhr()
    login.login()
    login.nav_menu()
