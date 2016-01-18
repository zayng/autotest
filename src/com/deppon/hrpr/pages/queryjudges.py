# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from com.deppon.hrpr.pages.page import Page


class QueryJudges(Page):

    def empty_rect(self):
        self.sleep(2)
        rect_mnts = self.driver.find_elements_by_xpath("//button[span[text()='清空收件人']]")
        rect_mnts.pop().click()

    def queryempcode(self, *empcode):
        for emp in range(len(empcode)):
            self.sleep(3)
            emp_mnts = self.driver.find_elements_by_xpath("//input[@name='number']")
            emp_mnt = emp_mnts.pop()
            emp_mnt.clear()
            emp_mnt.send_keys(empcode[emp])

            querybutton = "//div[contains(@id,'button') and @style='border-width: 1px; left: 293px; " \
                          "margin:0px; top: 0px; width: 75px;']//button[span[text()='查询']]"
            self.driver.find_elements_by_xpath(querybutton).pop().click()
            self.sleep(3)
            self.driver.find_elements_by_xpath("//tr[count(td)=10]/td[1]").pop().click()
            check_str = "//div[em[button[span[text()='清空收件人']]]]/preceding-sibling::div//button[span" \
                        "[text()='确定']]"
            self.sleep(1)
            self.driver.find_elements_by_xpath(check_str).pop().click()
        close_mnt = self.driver.find_elements_by_xpath("//button[span[text()='关闭']]")
        close_mnt.pop().click()

    def queryjudges(self, *empcode):
        self.empty_rect()
        self.queryempcode(*empcode)

