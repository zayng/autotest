# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from com.deppon.hrpr.pages.page import Page

class SelectClass(Page):

    def selectclassname(self, key):
        authlist_loc = "//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]"
        authlist_mnt = self.driver.find_elements_by_xpath(authlist_loc)
        if len(authlist_mnt) == 1:
            authlist_mnt.pop().click()
        else:
            authlist_mnt.pop(key).click()

    def select_authlist_page(self, key=0):
        self.selectclassname(key)
