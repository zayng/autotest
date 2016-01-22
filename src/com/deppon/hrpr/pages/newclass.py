"""
Created on 2015年11月2日

@author: 119937
"""
import random
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from com.deppon.hrpr.pages.common import Support


class AddClassName(Support):
    """
    页面功能：新增认证开班
    """
    classbtn_loc = "//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]"
    classname_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='classname']"
    classaddr_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='address']"

    def cla_btn_element(self):
        """点击新增班级按钮"""
        self.sleep(2)
        self.driver.find_element_by_xpath(self.classbtn_loc).click()

    def cla_name_element(self, classname):
        """填写班级名称"""
        if classname is None:
            self.driver.find_element_by_xpath(self.classname_loc).send_keys(self.genera_classname())
        else:
            self.driver.find_element_by_xpath(self.classname_loc).send_keys(classname)

    def cla_addr_element(self, classaddr):
        """填写开班地点"""
        if classaddr is None:
            self.driver.find_element_by_xpath(self.classaddr_loc).send_keys(self.genera_classname(fno=False))
        else:
            self.driver.find_element_by_xpath(self.classaddr_loc).send_keys(classaddr)

    def add_classname_page(self, classname, classaddr):
        self.cla_btn_element()
        self.cla_name_element(classname)
        self.cla_addr_element(classaddr)

    def down_large_element(self, large):
        """选择新增班级的认证大类"""
        driver = self.driver
        identifica_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']"
        # 选择认证大类
        driver.find_element_by_xpath(identifica_loc).click()
        driver.find_element_by_xpath("//ul[count(li)=13]/li[%s+1]" % large).click()

    def down_level_element(self, level):
        """
        选择新开班级的认证层级
        """
        driver = self.driver
        classlevel_loc = "//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']"
        # 选择认证层级
        driver.find_element_by_xpath(classlevel_loc).click()
        driver.find_element_by_xpath("//ul[count(li)=4]/li[%s+1]" % level).click()

    def written_results(self, large, level):
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

    def down_classlevel_page(self, large, level):
        """选择新开班级认证大类和层级，并根据大类和成绩设置笔试成绩或是专业影响力占比"""
        self.down_large_element(large)
        self.down_level_element(level)
        self.written_results(large, level)

    def addclass_begintime(self):
        begin_time = "//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(begin_time).click()
        self.select_datetime(fg=0)

    def addclass_endtime(self):
        end_time = "//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(end_time).click()
        self.select_datetime(23, 30, 20, yy=2016, mm=1, dd=27, fg=1)

    def set_datetime_page(self):
        """设置新开班级的开始时间和结束时间"""
        self.addclass_begintime()
        self.addclass_endtime()

    def save_class(self):
        """保存新增班级"""
        savecla = self.driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
        savecla.click()
        self.sleep(3)
        rmsg = "//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        conf_elem = WebDriverWait(self.driver, 3).until(ex.presence_of_element_located((By.XPATH, rmsg)))
        conf_elem.click()

    def save_classname_page(self):
        self.save_class()

    def add_newclass_page(self, classname=None, classaddr=None, large=0, level=0):
        """包含新增班级所有页面操作
        :param classname: 班级名称
        :param classaddr: 班级地点
        :param large: 认证大类
        :param level: 认证层级
        """
        self.log.info("开始新增认证班级操作")
        self.add_classname_page(classname, classaddr)
        self.down_classlevel_page(large, level)
        self.set_datetime_page()
        self.save_classname_page()

    def is_element_present_success(self):
        success_msg = "//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
        try:
            self.driver.find_element_by_xpath(success_msg)
        except (NoSuchElementException, TimeoutException) as e:
            self.log.info(e)
            return False
        return True

    def is_element_present_required(self):
        required_msg = "//div[contains(@id,'messagebox')]//div[contains(text(),'必输项为空或输入有误!')]"
        try:
            self.driver.find_element_by_xpath(required_msg)
        except (NoSuchElementException, TimeoutException) as e:
            self.log.info(e)
            return False
        return True

    @staticmethod
    def write_classname(*args):
        """保存新增班级信息到文件
        args: 班级名称，认证大类，认证层级，TS
        """
        filename = os.path.abspath(r"../temp/class-name.dat")
        with open(filename, 'a') as f:
            f.writelines("%s#%s#%s#'%s'\n" % args)

    @staticmethod
    def genera_classname(fno=True):
        if fno:
            return "2015年第%r期认证开班" % random.randint(1, 9999)
        else:
            return "德邦学院D%r" % random.randint(100, 200)
