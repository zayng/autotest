# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
from time import sleep

from com.deppon.hrpr.pageobj.login import Login126


def test_user_login(driver, username, password):
    """测试登陆126邮箱"""

    login_page = Login126(driver)
    login_page.open()
    login_page.type_user(username)
    login_page.type_pwd(password)
    login_page.submit()
    sleep(3)
    assert (username == 'suesce@126.com'), "用户名称不匹配，登陆失败"
