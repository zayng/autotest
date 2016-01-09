# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
from time import sleep

from selenium import webdriver

from com.deppon.hrpr.page.page import Page


class Login126(Page):
    """
    登录www.126.com页面
    """

    def opennhr(self):
        self.open()

    def login(self, user="231432", password="qqqqqq"):
        self.log.info("使用账号登陆NHR系统")
        self.log.info(user + ',' + password)
        self.driver.find_element_by_id("loginName").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("a_login").click()

    def nav_menu(self, s=2):
        self.log.info("开始打开NHR菜单节点：HR单据申请-储备认证管理-认证管理-认证开班管理。")
        sleep(s)
        self.driver.find_element_by_xpath("//div[text()='HR单据申请']").click()
        sleep(s)
        self.driver.find_element_by_xpath("//div[text()='储备认证管理']").click()
        sleep(s)
        self.driver.find_element_by_xpath("//div[text()='认证管理']").click()
        sleep(s)
        self.driver.find_element_by_xpath("//div[text()='认证开班管理']").click()
        sleep(s + 1)


if __name__ == '__main__':
    login = Login126()
    login.opennhr()
    login.login()
    login.nav_menu()
