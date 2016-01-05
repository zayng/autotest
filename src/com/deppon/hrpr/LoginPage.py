# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from com.deppon.hrpr.page import Page


class Login126(Page):
    """
    登录www.126.com页面
    """
    uri = " "

    # 定位元素
    username = (By.ID, 'idInput')
    password = (By.ID, 'pwdInput')
    loginbtn = (By.ID, 'loginBtn')

    # action

    def open(self):
        self._open(self.uri)

    def type_user(self, user):
        self.find_element(*self.username).send_keys(user)

    def type_pwd(self, pwd):
        self.find_element(*self.pwssword).send_keys(pwd)

    def submit(self):
        self.find_element(*self.loginbtn).click()


if __name__ == 'main__':
    driver = webdriver.Firefox()
    login = Login126(driver)
    login.open()
    login.type_user("suesce@126.com")
    login.type_pwd("112200")
    login.submit()
