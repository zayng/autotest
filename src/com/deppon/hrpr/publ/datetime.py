# -*- coding:utf-8 -*-
"""
Created on 2015年11月3日

@author: 119937
"""
from selenium.webdriver.common.action_chains import ActionChains
from com.deppon.hrpr.pages.newclass import Page


class DateObj(Page):
    """将日期控件封装成单独的页面对象"""

    def calendar(self, *dptime, **dpdate):
        """用于界面选择日期"""
        driver = self.driver
        self.sleep(2)
        frabegin = driver.find_element_by_xpath("//*[@width='97' and @height='9']")
        driver.switch_to_frame(frabegin)
        # driver.switch_to_frame(0)
        if len(dpdate) > 1:
            sdate = driver.find_element_by_xpath(
                    "//td[@onclick='day_Click(%s,%s,%s);']" % (dpdate['yy'], dpdate['mm'], dpdate['dd']))
            sdate.click()
        elif dpdate['fg'] != 0:
            year, month, day = (2015, 11, 5)
            sdate = driver.find_element_by_xpath(u"//td[@onclick='day_Click(%s,%s,%s);']" % (year, month, day))
            sdate.click()
        if len(dptime) > 0:
            hour = driver.find_element_by_xpath("//input[@class='tB']")
            ActionChains(driver).double_click(hour).perform()
            hour.send_keys(dptime[0])
            mins = driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[3]")
            ActionChains(driver).double_click(mins).perform()
            mins.send_keys(dptime[1])
            ss = driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[last()]")
            ActionChains(driver).double_click(ss).perform()
            ss.send_keys(dptime[2])
        if dpdate['fg']:
            driver.find_element_by_id("dpOkInput").click()
        else:
            driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()
