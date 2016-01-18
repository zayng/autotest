# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""

from com.deppon.hrpr.page.page import Page
from com.deppon.hrpr.page.common import Support
from com.deppon.hrpr.page.queryjudges import QueryJudges

class AddTask(Page, Support, QueryJudges):

    def notice_judges(self):
        """点击评委通知按钮"""
        self.sleep(2)
        self.driver.find_element_by_xpath(u"//button[span[text()='评委通知']]").click()

    def add_task(self):
        """添加测评任务-认证面谈"""
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype1-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='认证面谈']").click()

    def add_taskname(self, taskname):
        """填写任务名称"""
        self.sleep(2)
        taskname_mnt = self.driver.find_element_by_xpath("//input[@name='taskname']")
        taskname_mnt.send_keys(taskname)

    def task_begintime(self):
        """选择任务开始时间"""
        self.sleep(2)
        self.driver.find_element_by_xpath("//table[@id='judgebegintime-triggerWrap']//td[2]").click()
        self.select_datetime(10, 45, 22, yy=2016, mm=1, dd=5, fg=1)

    def task_results(self, share):
        """设置任务成绩占比"""
        taskratio = self.driver.find_element_by_xpath("//input[@name='taskratio']")
        taskratio.clear()
        taskratio.send_keys(share)

    def add_judges(self, *empcode):
        """添加任务评委"""
        mailto_loc = "//td[@id='mailTo-inputCell']/following-sibling::td"
        self.driver.find_element_by_xpath(mailto_loc).click()
        self.queryjudges(*empcode)

    def mailto(self):
        """评委邮件发送 """
        inform = self.driver.find_element_by_xpath("//button[@id='informjudgebutton-btnEl']")
        inform.click()
        self.sleep(3)

    def save_task(self):
        """保存任务"""
        msg_loc = "//div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        self.sleep(2)
        self.driver.find_element_by_xpath("//button[@id='savejudgebutton-btnEl']").click()
        self.driver.find_element_by_xpath().click(msg_loc)

    def close_task(self):
        """关闭评委任务页面"""
        self.sleep(2)
        retn_loc = "//div[@id='savejudgebutton']/following-sibling::div//button"
        self.driver.find_element_by_xpath(retn_loc).click()

    def add_certitask_page(self, taskname, empcode=('119937', '116460', '000120', '000121')):
        self.notice_judges()
        self.add_task()
        self.add_taskname(taskname)
        self.task_begintime()
        self.add_judges(*empcode)
        self.save_task()
        self.close_task()

    def add_repottask_page(self):
        pass

