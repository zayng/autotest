# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from com.deppon.hrpr.pages.page import Page

class SelectClass(Page):

    def selectclassname(self, key=-1):
        authlist_locs = "//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]"
        authlist_mnts = self.driver.find_elements_by_xpath(authlist_locs)
        authlist_mnts.pop(key).click()

    def select_authlist_page(self, key=0):
        self.log.info("开始选择认证班级操作")
        self.selectclassname(key)

    def save_classinfo(self, key=-1):
        """保存被选中班级的信息"""
        texts = []
        authlist_child_locs = "//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]/tr/div"
        tr14 = self.driver.find_elements_by_xpath(authlist_child_locs)
        for tr in tr14:
            text = tr.text
            texts.append(text)
            print(text, "==>", texts)
