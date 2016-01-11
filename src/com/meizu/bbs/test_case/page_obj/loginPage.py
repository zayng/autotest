# -*- coding:utf-8 -*-
"""
Created on '2016/1/11'

@author: '119937'
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    """
    用户登录界面
    """
    url = '/'

    # action

    bbs_login_user_loc = (By.XPATH, "//div[@id='mzCust']/div/img")
    bbs_login_button_loc = (By.ID, "mzLogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(2)
        self.find_element(*self.bbs_login_button_loc)

    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "login")

    # 登录用户名

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
            self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 登录
    def user_login(self, username="username", password="1111"):
        """获取用户和密码登录"""
        self.open()
        self.bbs_login()
        self.login_username()
        self.login_password()
        self.login_password()
        self.login_button()
        sleep(2)

    user_error_hint_loc = (By.XPATH, "//span[@for='account']" )
    pawd_error_hint_loc = (By.XPATH, "//span[@for='password']")
    user_login_success_loc = (By.ID, "mzCustName")

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text