# -*- coding:utf-8 -*-
"""
Created on '2016/1/4'

@author: '119937'
"""


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

class Page(object):
    """
    页面类基类，用于所有页面的继承。
    """
    login_url = 'http://www.126.com'

    def __init__(self, driver, base_url=login_url, parent=None):
        self.base_url = base_url
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.timeout = 30
        self.parent = parent
        self.tabs = {}

    def _open(self, uri):
        self.all_url = self.base_url + uri
        self.driver.get(self.all_url)
        self.driver.maximize_window()
        assert self.on_page(), "Did not land on  %s " % self.all_url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self):
        self._open(self.uri)

    def on_page(self):
        return self.driver.current_url == self.all_url

    def script(self, scr):
        self.driver.execute_script(scr)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).click()
            self.driver.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s page does not have '%s' locator" % (self, loc))

# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     login = Page(driver)
#     login.uri = '/'
#     login.open()
