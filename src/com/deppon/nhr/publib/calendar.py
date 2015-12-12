# -*- coding:utf-8 -*-
'''
Created on 2015年11月3日

@author: 119937
'''
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from com.deppon.nhr import log

def calendar(driver,*dptime,**dpdate):
    ''' 
            用于选择日历控件选择日期
    '''
#    year,month,day=(2015,11,5)
    # 切换到日期控件
    log.info("切换到日历控件选择日期")
    
    frabegin=driver.find_element_by_xpath(u"//*[@width='97' and @height='9']")
    driver.switch_to_frame(frabegin)
    # driver.switch_to_frame(0)
    sleep(1)
    # 选择日期
    log.info("选择日期")
    if len(dpdate)>1:      
        sDate=driver.find_element_by_xpath(u"//td[@onclick='day_Click(%s,%s,%s);']" % (dpdate['yy'],dpdate['mm'],dpdate['dd']))
        sDate.click()
    elif dpdate['fg'] != 0:
        year,month,day=(2015,11,5)
        sDate=driver.find_element_by_xpath(u"//td[@onclick='day_Click(%s,%s,%s);']" % (year,month,day))
        sDate.click()
 
    # ActionChains(driver).double_click(seTime).perform()
    # 选择时间
    log.info("选择时间")
    if len(dptime)>0:      
        hour=driver.find_element_by_xpath("//input[@class='tB']")
        ActionChains(driver).double_click(hour).perform()
        hour.send_keys(dptime[0])
        min=driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[3]")
        ActionChains(driver).double_click(min).perform()
        min.send_keys(dptime[1])
        ss=driver.find_element_by_xpath("//span[@id='dpTimeStr']/following-sibling::input[last()]")
        ActionChains(driver).double_click(ss).perform()
        ss.send_keys(dptime[2])
       
    # 点击确定
    if dpdate['fg']:
        driver.find_element_by_id("dpOkInput").click()
        log.info("点击时间控件确定按钮")
    else:
        driver.find_element_by_id("dpTodayInput").click()
        log.info("选择今天时间")
    
    # 切换表单
    log.info("选择日期结束，结束调用")
    driver.switch_to_default_content()
