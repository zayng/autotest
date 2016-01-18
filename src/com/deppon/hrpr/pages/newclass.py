"""
Created on 2015年11月2日

@author: 119937
"""
import random
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

from com.deppon.hrpr.pages.page import Page
from com.deppon.hrpr.pages.common import Support


class AddClassName(Page, Support):
    """
    页面功能：新增认证开班
    """
    # By Xapth
    classbtn_loc = "//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]"
    classname_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='classname']"
    classaddr_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='address']"

    def cla_btn_element(self):
        self.sleep(2)
        self.driver.find_element_by_xpath(self.classbtn_loc).click()

    def cla_name_element(self):
        self.driver.find_element_by_xpath(self.classname_loc).send_keys(self.genera_name())

    def cla_addr_element(self):
        self.driver.find_element_by_xpath(self.classaddr_loc).send_keys(self.genera_name(fno=False))

    def add_classname_page(self):
        self.cla_btn_element()
        self.cla_name_element()
        self.cla_addr_element()

    def add_classname(self):
        """
        在班级列表，点击新增按钮添加新班级
        """
        driver = self.driver
        cla_btn = driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]")
        cla_btn.click()
        classna = driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='classname']")
        classna.send_keys(self.genera_name())
        address = driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='address']")
        address.send_keys(self.genera_name(False))

    def down_level(self, large, level):
        """
        选择新开班级的认证大类和认证层级
        """
        driver = self.driver
        # 点击认证大类下拉选择框
        driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']").click()
        # 选择具体大类 //body/div[contains(@id,'boundlist')]//li[text()='IT类']
        driver.find_element_by_xpath("//ul[count(li)=13]/li[%s+1]" % large).click()
        # 点击认证层级下拉选择框
        driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']").click()
        # 选择层级
        driver.find_element_by_xpath("//ul[count(li)=4]/li[%s+1]" % level).click()

    def down_large_element(self, large, level):
        """选择新增班级的认证大类和认证层级"""
        driver = self.driver
        # 元素管理：认证大类下拉选择框，认证层级下拉选择框
        identifica_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']"
        classlevel_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']"
        # 选择认证大类
        driver.find_element_by_xpath(identifica_loc).click()
        driver.find_element_by_xpath("//ul[count(li)=13]/li[%s+1]" % large).click()
        # 选择认证层级
        driver.find_element_by_xpath(classlevel_loc).click()
        driver.find_element_by_xpath("//ul[count(li)=4]/li[%s+1]" % level).click()

    def written_exam(self, large, level):
        """认证笔试成绩分为专业笔试和专业影响力，系统默认笔试成绩占比20%，专业影响力占比10%。
         0-中级，1-高级，2-资深，3-专家
         其中IT类，IT需求与规划序列，IT研发序列认证笔试成绩占比为0.
        """
        if level in [0, 1, 2]:
            # 专业笔试成绩
            writtenratio = self.driver.find_element_by_name("writtenratio")
            writtenratio.clear()
            if large in range(4, 7):
                writtenratio.send_keys(0)
            else:
                writtenratio.send_keys(20)
        elif level == 3:
            # 专业影响力
            majorratio = self.driver.find_element_by_name("majorratio")
            majorratio.clear()
            majorratio.send_keys(10)

    def select_level_page(self, large, level):
        self.down_level(large, level)
        self.written_exam(large, level)

    def addclass_begintime(self):
        begin_time = "//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(begin_time).click()
        self.select_datetime(fg=0)

    def addclass_endtime(self):
        end_time = "//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(end_time).click()
        self.select_datetime(23, 30, 20, yy=2016, mm=1, dd=27, fg=1)

    def select_date_page(self):
        self.addclass_begintime()
        self.addclass_endtime()

    def save_class(self):
        # 保存新增班级
        savecla = self.driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
        savecla.click()
        self.sleep(3)
        # smsg = "//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
        rmsg = "//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        conf_elem = WebDriverWait(self.driver, 5).until(ex.presence_of_element_located((By.XPATH, rmsg)))
        conf_elem.click()

    def save_classname_page(self):
        self.save_class()

    def classname_page(self, large, level):
        """包含新增班级所有页面操作 """
        self.add_classname_page()
        self.select_level_page(large, level)
        self.select_date_page()
        self.save_classname_page()

    @staticmethod
    def write_classname(*args):
        """保存新增班级信息到文件
        args: 班级名称，认证大类，认证层级，TS
        """
        filename = os.path.abspath(r"../temp/class-name.dat")
        with open(filename, 'a') as f:
            f.writelines("%s#%s#%s#'%s'\n" % args)

    @staticmethod
    def genera_name(fno=True):
        if not fno:
            return "德邦学院D%r" % random.randint(100, 200)
        return "2015年第%r期认证开班" % random.randint(1, 9999)

if __name__ == '__main__':
    pass