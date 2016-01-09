"""
Created on 2015年11月2日

@author: 119937
"""
from time import sleep
from datetime import datetime
import random
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

from com.deppon.hrpr.page.page import Page
from com.deppon.hrpr.page.dateobj import DateObj


class AddClass(Page):
    """
    页面功能：新增认证开班
    """

    def new_classname(self):
        """
        在班级列表，点击新增按钮添加新班级
        """
        driver = self.driver
        # 点击新开班按钮
        cla_btn = driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]")
        cla_btn.click()
        # 输入新开班级名称
        classna = driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='classname']")
        classna.send_keys(self.randname())
        # 输入新开班级地点
        address = driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='address']")
        address.send_keys(self.randname(False))

    def down_level(self):
        """
        选择新开班级的认证大类和认证层级
        """
        driver = self.driver
        # 点击认证大类下拉选择框
        driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']").click()
        # 选择具体大类 //body/div[contains(@id,'boundlist')]//li[text()='IT类']

        driver.find_element_by_xpath("//ul[count(li)=13]/li[%s+1]" % self.large).click()
        # 点击认证层级下拉选择框
        driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']").click()
        # 选择层级
        driver.find_element_by_xpath("//ul[count(li)=4]/li[%s+1]" % self.level).click()

    def written_exam(self):
        if self.level in [0, 1, 2]:
            # 专业笔试成绩
            writtenratio = self.driver.find_element_by_name("writtenratio")
            writtenratio.clear()
            if self.large in range(4, 7):
                writtenratio.send_keys(0)
            else:
                writtenratio.send_keys(20)
        elif self.level == 3:
            # 专业影响力
            majorratio = self.driver.find_element_by_name("majorratio")
            majorratio.clear()
            majorratio.send_keys(10)

    def choose_time(self):
        driver = self.driver
        begin_time = "//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]"
        driver.find_element_by_xpath(begin_time).click()

        # 调用时间控件选择开始时间
        DateObj.calendar(driver, fg=0)
        # 选择结束时间
        newed = driver.find_element_by_xpath(u"//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]")
        newed.click()
        # 调用时间控件选择结束时间
        calendar(driver, 23, 30, 20, yy=2016, mm=1, dd=9, fg=1)
        # 保存新开班级
        saclass = driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
        saclass.click()
        sydate = datetime.now().strftime('%Y-%m-%d %X')
        sleep(4)
        # 获取提示信息，如果保存成功，保存班级名称
        message = u"//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
        msg = WebDriverWait(driver, 10).until(ex.text_to_be_present_in_element((By.XPATH, message), u'保存成功'))
        # 确定保存
        log.info("新增班级成功，新增班级名称：" + name)
        rk = u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        element = WebDriverWait(driver, 10).until(ex.presence_of_element_located((By.XPATH, rk)))
        element.click()

    @staticmethod
    def wclassname(*args):
        """保存新增班级信息到文件
        :param args: 班级名称，认证大类，认证层级，TS
        """
        filename = os.path.abspath(r"../temp/class-name.dat")
        with open(filename, 'a') as f:
            f.writelines("%s#%s#%s#'%s'\n" % args)

    @staticmethod
    def randname(fno=True):
        if not fno:
            return "德邦学院D%r" % random.randint(100, 200)
        return "2015年第%r期认证开班" % random.randint(1, 9999)

if __name__ == "__main__":
    self = startup
    startup(self)
    login(self)
    menu(self)
    newclass(self)
