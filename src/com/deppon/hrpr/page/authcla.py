"""
Created on 2015年11月2日

@author: 119937
"""
import random
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ex

from com.deppon.hrpr.page.page import Page


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
        """认证笔试成绩分为专业笔试和专业影响力，系统默认笔试成绩占比20%，专业影响力占比10%。
         0-中级，1-高级，2-资深，3-专家
         其中IT类，IT需求与规划序列，IT研发序列认证笔试成绩占比为0.
        """
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

    def begin_date(self):
        begin_time = "//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(begin_time).click()
        self.select_date(fg=0)

    def end_date(self):
        end_time = "//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]"
        self.driver.find_element_by_xpath(end_time).click()
        self.select_date(23, 30, 20, yy=2016, mm=1, dd=27, fg=1)

    def save_class(self):

        savecla = self.driver.find_element_by_xpath("//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
        savecla.click()
        self.sleep(3)
        smsg = "//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
        rmsg = "//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        conf_elem = WebDriverWait(self.driver, 5).until(ex.presence_of_element_located((By.XPATH, rmsg)))
        conf_elem.click()

    def select_date(self, *dptime, **dpdate):
        """用于界面选择日期"""
        driver = self.driver
        self.sleep(2)
        frabegin = driver.find_element_by_xpath("//*[@width='97' and @height='9']")
        driver.switch_to_frame(frabegin)
        # driver.switch_to_frame(0)
        if len(dpdate) > 1:
            sdate = driver.find_element_by_xpath("//td[@onclick='day_Click(%s,%s,%s);']"
                                                 % (dpdate['yy'], dpdate['mm'], dpdate['dd']))
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

    @staticmethod
    def write_classname(*args):
        """保存新增班级信息到文件
        :param args: 班级名称，认证大类，认证层级，TS
        """
        filename = os.path.abspath(r"../temp/class-name.dat")
        with open(filename, 'a') as f:
            f.writelines("%s#%s#%s#'%s'\n" % args)

    @staticmethod
    def genera_name(fno=True):
        if not fno:
            return "德邦学院D%r" % random.randint(100, 200)
        return "2015年第%r期认证开班" % random.randint(1, 9999)
