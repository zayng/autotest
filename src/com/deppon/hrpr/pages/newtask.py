# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# from com.deppon.hrpr.pages.page import Page
from com.deppon.hrpr.pages.common import Support
from com.deppon.hrpr.pages.queryjudges import QueryJudges


class AddTask(QueryJudges, Support):
    def notice_judges(self):
        """点击评委通知按钮"""
        self.sleep(2)
        self.driver.find_element_by_xpath(u"//button[span[text()='评委通知']]").click()

    def add_task_type1(self):
        """认证层级：中级，高级
        添加测评任务-认证面谈
        """
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype1-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='认证面谈']").click()

    def add_task_type2(self):
        """认证层级：资深
        添加测评任务-认证面谈
        """
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype2-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='认证面谈']").click()

    def add_repottask_type2(self):
        """认证层级：资深
        添加测评任务-认证面谈
        """
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype2-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='课题汇报']").click()

    def add_task_type3(self):
        """认证层级：专家
        添加测评任务-课题汇报
        """
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype3-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='课题汇报']").click()

    def is_authtasktype1_present(self):
        authtasktype1 = "//td[@id='authtasktype1-inputCell']"
        try:
            self.sleep(1)
            is_type1 = self.driver.find_element_by_xpath(authtasktype1).is_displayed()
            if is_type1:
                return True
            else:
                return False
        except (NoSuchElementException, TimeoutException) as e:
            return False

    def is_authtasktype2_present(self):
        authtasktype2 = "//td[@id='authtasktype2-inputCell']"
        try:
            self.sleep(1)
            is_type2 = self.driver.find_element_by_xpath(authtasktype2).is_displayed()
            if is_type2:
                return True
            else:
                return False
        except (NoSuchElementException, TimeoutException) as e:
            return False

    def is_authtasktype3_present(self):
        authtasktype3 = "//td[@id='authtasktype3-inputCell']"
        try:
            self.sleep(1)
            is_type3 = self.driver.find_element_by_xpath(authtasktype3).is_displayed()
            if is_type3:
                return True
            else:
                return False
        except (NoSuchElementException, TimeoutException) as e:
            return False

    def add_reporttask(self):
        """添加测评任务-演讲面谈"""
        self.sleep(2)
        self.driver.find_element_by_xpath("//td[@id='authtasktype1-inputCell']").click()
        self.driver.find_element_by_xpath("//li[text()='课题汇报']").click()

    def add_taskname(self, taskname):
        """填写任务名称"""
        self.sleep(2)
        taskname_mnt = self.driver.find_element_by_xpath("//input[@name='taskname']")
        taskname_mnt.clear()
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
        self.driver.find_element_by_xpath(msg_loc).click()

    def close_task(self):
        """关闭评委任务页面"""
        self.sleep(2)
        retn_loc = "//div[@id='savejudgebutton']/following-sibling::div//button"
        self.driver.find_element_by_xpath(retn_loc).click()

    def add_certitask_page(self, taskname, *empcode):
        self.log.info("开始添加认证面谈")
        if self.is_authtasktype1_present():
            self.add_task_type1()
        if self.is_authtasktype2_present():
            self.add_task_type2()
        self.add_taskname(taskname)
        self.task_begintime()
        self.add_judges(*empcode)
        self.save_task()

    def add_repottask_page(self, taskname, *empcode):
        self.log.info("开始添加课题汇报")
        if self.is_authtasktype2_present():
            self.add_repottask_type2()
        if self.is_authtasktype3_present():
            self.add_task_type3()
        self.add_taskname(taskname)
        self.task_begintime()
        self.add_judges(*empcode)
        self.save_task()

    def add_task_page(self, taskname=None, empcode=('119937', '116460', '000120', '000121')):
        """开始添加测评任务以及评委操作
        :param taskname: 定义任务名称，默认使用随机生成任务名称
        :param empcode: 评委工号
        """
        self.log.info("开始添加测评任务以及评委操作")
        self.notice_judges()
        if self.is_authtasktype1_present() or self.is_authtasktype2_present():
            if taskname is None:
                taskname = self.genera_taskname()
            self.add_certitask_page(taskname, *empcode)
        if self.is_authtasktype2_present() or self.is_authtasktype3_present():
            if taskname is None:
                taskname = self.genera_taskname(task_type=False)
            self.add_repottask_page(taskname, *empcode)
        self.close_task()

    @staticmethod
    def genera_taskname(task_type=True):
        if task_type:
            return "认证面谈%s" % random.randint(100, 200)
        else:
            return "课题汇报%s" % random.randint(200, 400)
