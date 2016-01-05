"""
Created on 2015年11月5日

@author: 119937
"""

from time import sleep
from random import randint

from com.deppon.hrss.publ.log4 import log
from com.deppon.hrss.globalvar import globalvar
from com.deppon.hrss.publ.calendar import calendar
from com.deppon.hrss.publ.query import queryclass, selectcla, queryjudges
from com.deppon.hrss.func.login import startup, login, menu



def task(self):
    """填写测评任务和评委
    :param self:
    :return: 无
    """
    driver = self.driver
    log.info("开始添加测评任务")
    # 点击评委通知按钮
    driver.find_element_by_xpath(u"//button[span[text()='评委通知']]").click()

    # 选择测评任务
    driver.find_element_by_xpath("//td[@id='authtasktype1-inputCell']").click()

    # 选择测评任务
    driver.find_element_by_xpath(u"//li[text()='认证面谈']").click()
    sleep(2)
    # 填写测评名称
    tasktext = u'认证面谈%s' % randint(100, 1000)
    taskname = driver.find_element_by_xpath("//input[@name='taskname']")
    taskname.send_keys(tasktext)

    # 调用选择日期控件函数calendar
    driver.find_element_by_xpath("//table[@id='judgebegintime-triggerWrap']//td[2]").click()
    calendar(driver, 10, 45, 22, yy=2016, mm=1, dd=5, fg=1)

    # 填写任务成绩占比
    taskratio = driver.find_element_by_xpath("//input[@name='taskratio']")
    taskratio.clear()
    taskratio.send_keys(100)

    '''
    # 勾选剔除最高排名
    highrank = driver.find_element_by_xpath(u"//label[text()='剔除最高排名']/preceding-sibling::input")
    highrank.click()

    # 勾选剔除最低排名
    lowrank = driver.find_element_by_xpath(u"//label[text()='剔除最低排名']/preceding-sibling::input")
    lowrank.click()
    '''
    # 查询评委工号
    driver.find_element_by_xpath("//td[@id='mailTo-inputCell']/following-sibling::td").click()

    # call queryjudges.在查询界面选择评委工号
    queryjudges(driver, '119937', '116460', '000120', '000121')

    # 保存任务
    driver.find_element_by_xpath("//button[@id='savejudgebutton-btnEl']").click()

    #     #邮件发送
    #     inform=driver.find_element_by_xpath("//button[@id='informjudgebutton-btnEl']")
    #     inform.click()

    # 保存任务成功，点击确定
    driver.find_element_by_xpath("//div[contains(@id,'messagebox')]//button[span[text()='确定']]").click()

    # 返回班级列表界面
    driver.find_element_by_xpath("//div[@id='savejudgebutton']/following-sibling::div//button").click()


if __name__ == '__main__':
    self = startup
    self = startup
    startup(self)
    login(self)
    menu(self)
    queryclass(self, li=2, le=1)
    selectcla(self)
    task(self)
