# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from com.deppon.hrpr.pages.page import Page

class Support(Page):

    def select_datetime(self, *dptime, **dpdate):
        """用于界面选择日期"""
        driver = self.driver
        self.sleep(2)
        frabegin = driver.find_element_by_xpath("//*[@width='97' and @height='9']")
        driver.switch_to_frame(frabegin)
        # driver.switch_to_frame(0)
        if len(dpdate) > 1:
            dd = driver.find_element_by_xpath("//td[@onclick='day_Click(%s,%s,%s);']"
                                              % (dpdate['yy'], dpdate['mm'], dpdate['dd']))
            dd.click()
        elif dpdate['fg'] != 0:
            year, month, day = (2015, 11, 5)
            dd = driver.find_element_by_xpath("//td[@onclick='day_Click(%s,%s,%s);']" % (year, month, day))
            dd.click()
        if len(dptime) > 0:
            hour = driver.find_element_by_xpath("//input[@class='tB']")
            ActionChains(driver).double_click(hour).perform()
            hour.send_keys(dptime[0])
            mm = driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[3]")
            ActionChains(driver).double_click(mm).perform()
            mm.send_keys(dptime[1])
            ss = driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[last()]")
            ActionChains(driver).double_click(ss).perform()
            ss.send_keys(dptime[2])
        if dpdate['fg']:
            driver.find_element_by_id("dpOkInput").click()
        else:
            driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()

    def selectclassname(self, key=-1):
        authlist_locs = "//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]"
        authlist_mnts = self.driver.find_elements_by_xpath(authlist_locs)
        authlist_mnts.pop(key).click()

    def select_authlist_page(self, key=0):
        self.log.info("开始选择认证班级操作")
        self.selectclassname(key)

