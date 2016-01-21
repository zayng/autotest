# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from com.deppon.hrpr.pages.page import Page


class QueryClass(Page):

    def queryclassname(self, classname):
        """ 班级名称查询
        :param classname: 查询班级名称
        """
        # by xpath
        classname_loc = "//div[@id='T_authinfo-authClassMng']//input[@name='classname']"
        self.sleep(2)
        classname_mnt = self.driver.find_element_by_xpath(classname_loc)
        classname_mnt.clear()
        classname_mnt.send_keys(classname)

    def querylarge(self, large):
        """选择查询的认证大类"""
        identi_loc = "//div[@id='T_authinfo-authClassMng']//input[@name='identificationkind']"
        self.sleep(2)
        self.driver.find_element_by_xpath(identi_loc).click()
        li_element = self.driver.find_elements_by_xpath("//ul[count(li)>=13]/li[%s+1]" % large).pop()
        li_element.click()

    def queryclasslevel(self, level):
        """选择查询的认证层级"""
        classlevel_loc = "//div[@id='T_authinfo-authClassMng']//input[@name='classlevel']"
        self.sleep(1)
        self.driver.find_element_by_xpath(classlevel_loc).click()
        level_element = self.driver.find_elements_by_xpath("//ul[count(li)=4]/li[%s+1]" % level).pop()
        level_element.click()

    def queryauthinfo(self):
        """点击查询按钮 """
        query_loc = "//div[@id='T_authinfo-authClassMng']//button[span[text()='查询']]"
        self.sleep(1)
        self.driver.find_element_by_xpath(query_loc).click()

    def queryclass_page(self, **cla):
        """班级查询操作"""
        self.log.info("开始查询认证班级操作")
        if 'classname' in cla.keys():
            self.queryclassname(cla['classname'])
        self.querylarge(cla['large'])
        self.queryclasslevel(cla['level'])
        self.queryauthinfo()
