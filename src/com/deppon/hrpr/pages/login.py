# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
from com.deppon.hrpr.pages.page import Page


class LoginNHR(Page):
    """
    登录nhr.deppon.com页面
    """

    def opennhr(self):
        self.open()

    def login(self, user="231432", pwd="qqqqqq"):
        """输入用户和密码"""
        username = self.driver.find_element_by_id("loginName")
        password = self.driver.find_element_by_id("password")
        loginbtn = self.driver.find_element_by_class_name("a_login")
        username.send_keys(user)
        password.send_keys(pwd)
        loginbtn.click()

    def nav_menu(self):
        self.log.info("开始打开NHR菜单节点：HR单据申请-储备认证管理-认证管理-认证开班管理。")
        nav_dat = ['储备认证管理', '认证管理', '认证开班管理']
        dat = nav_dat
        for value in dat:
            self.sleep(3)
            self.driver.find_element_by_xpath("//div[text()='%s']" % value).click()
        else:
            self.sleep(2)
            self.log.info("NHR菜单节点打开完毕")

    def user_login(self, user="231432", pwd="qqqqqq"):
        self.log.info("使用账号登陆NHR系统")
        self.log.info(user + ',' + pwd)
        self.opennhr()
        self.login(user, pwd)
        self.nav_menu()

    @staticmethod
    def nav_dat():
        dat = ['储备认证管理', '认证管理', '认证开班管理']
        return dat

if __name__ == '__main__':
    login = LoginNHR()
    login.opennhr()
    login.login()
    login.nav_menu()
