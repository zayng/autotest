# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""
from com.deppon.hrpr.test_user_login import test_user_login
from selenium import webdriver


def main():
    try:
        # selenium
        driver = webdriver.Firefox()
        username = 'suesce@126.com'
        password = '112200'
        test_user_login(driver, username, password)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
