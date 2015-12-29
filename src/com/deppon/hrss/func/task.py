"""
Created on 2015年11月5日

@author: 119937
"""
from com.deppon.nhr.login.login import nhrLogin
from com.deppon.nhr.student.impstudent import selectcla, notice
from com.deppon.nhr.publib.query import queryclass, queryjudges
from com.deppon.nhr.publib.calendar import calendar

from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep


def task(driver):
    # 点击评委通知按钮
    driver.find_element_by_xpath(u"//button[span[text()='评委通知']]").click()

    # 选择测评任务
    driver.find_element_by_xpath("//td[@id='authtasktype1-inputCell']").click()

    # 选择测评任务
    driver.find_element_by_xpath(u"//li[text()='认证面谈']").click()
    sleep(1)
    # 填写测评名称
    tasktext = u'认证面谈%s' % randint(100, 1000)
    taskname = driver.find_element_by_xpath("//input[@name='taskname']")
    taskname.send_keys(tasktext)

    # 调用选择日期控件函数calendar
    driver.find_element_by_xpath("//table[@id='judgebegintime-triggerWrap']//td[2]").click()
    calendar(driver, 10, 45, 22, yy=2015, mm=11, dd=9, fg=1)

    # 填写任务成绩占比
    taskratio = driver.find_element_by_xpath("//input[@name='taskratio']")
    taskratio.clear()
    taskratio.send_keys(100)
    # 勾选剔除最高排名
    highrank = driver.find_element_by_xpath(u"//label[text()='剔除最高排名']/preceding-sibling::input")
    highrank.click()

    # 勾选剔除最低排名
    lowrank = driver.find_element_by_xpath(u"//label[text()='剔除最低排名']/preceding-sibling::input")
    lowrank.click()

    #    for item in range(4):
    # 查询评委工号
    driver.find_element_by_xpath("//td[@id='mailTo-inputCell']/following-sibling::td").click()

    # 调用员工查询界面
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
    login = nhrLogin()
    login.login()
    login.menu(2)
    driver = login.driver
    queryclass(driver, 3, 1)
    selectcla(driver, 7)
    #     notice(driver)
    task(driver)
