"""
Created on 2015年11月3日

@author: 119937
"""
import os

from selenium.webdriver.support.ui import WebDriverWait

from com.deppon.hrpr.pages.page import Page

class ImpStudent(Page):

    # By xpath
    def notice_student(self):
        """
        点击学员通知按钮，进入新增学员界面
        """
        notice_loc = "//div[@id='T_authinfo-authClassMng']//button[span[text()='学员通知']]"
        self.sleep(2)
        self.driver.find_element_by_xpath(notice_loc).click()

    def search_student(self, filename):
        """ 浏览本地计算机，填写学员模板所在路径
        :param filename 导入学员模板的路径，默认为temp/stuAuthImport.xlsx
        """
        stuexcel = self.driver.find_element_by_xpath("//input[@name='stuexcel']")
        try:
            self.sleep(2)
            stuexcel.send_keys(os.path.abspath(filename))
        except Exception as e:
            self.log.error("浏览学员Excel文件错误,异常信息" + str(e))

    def import_student(self):
        """点击导入按钮，并确定"""
        confirm_loc = "//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
        try:
            self.sleep(2)
            self.driver.find_element_by_xpath("//button[span[text()='导入']]").click()
            self.sleep(3)
            self.driver.find_element_by_xpath(confirm_loc).click()
        except Exception as e:
            self.log.error("导入学员文件错误，异常信息" + str(e))

    def revert_page(self):
        """返回新增学员界面"""
        return_loc = "//div[em[button[span[text()='邮件提醒']]]]/following-sibling::div//button[span[text()='返回']]"
        self.sleep(2)
        self.driver.find_element_by_xpath(return_loc).click()

    def imp_student_page(self, filename="../temp/stuAuthImport.xlsx"):
        """ 从本地Excel到入学员
        :param filename: 导入学员Excel文件路径
        """
        self.log.info("开始导入班级学员")
        self.notice_student()
        self.search_student(filename)
        self.import_student()
        self.revert_page()
