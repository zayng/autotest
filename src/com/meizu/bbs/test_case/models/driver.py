# -*- coding:utf-8 -*-
"""
Created on '2016/1/11'

@author: '119937'
"""
from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器驱动
def browser():
    FIREFOX = {
        "browserName": "firefox",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        "marionette": False,
    }
    host = "127.0.0.1:4444"
    CHROME = {"browserName": "chrome"}
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=CHROME)
    return driver


if __name__ == "__main__":
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
