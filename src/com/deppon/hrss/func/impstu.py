"""
Created on 2015年11月3日

@author: 119937
"""

from time import sleep
import os

from com.deppon.nhr.login.login import nhrLogin
from com.deppon.hrss.publ.query import queryclass, selectcla
from com.deppon.hrss import *


def notice(self):
    log.info("导入学员")

    driver = self.driver
    # 点击学员通知按钮
    notified = driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()"
                                            u"='学员通知']]")
    notified.click()

    # 浏览文件路径，浏览
    driver.find_element_by_xpath(u"//button[span[text()='浏览']]").click()
    # 调用uoloadfile.exe上传文件
    sleep(1)
    bin_home = os.path.abspath('../temp/uploadfile.exe')
    os.system(bin_home)
    # os.system("D:\\119937\\workspace\\autotest\\src\\com\\deppon\\nhr\\bin\\uploadfile.exe")

    # 浏览文件路径，input控件
    # inputfile=driver.find_element_by_xpath("//input[@name='']")
    # inputfile.send_keys(u"d:\\119937\\Desktop\\data\\stuAuthImport.xlsx")

    # 点击导入按钮
    driver.find_element_by_xpath(u"//button[span[text()='导入']]").click()
    sleep(2)

    # 导入成功
    driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]").click()

    # 返回班级列表
    re = driver.find_element_by_xpath(u"//div[em[button[span[text()='邮件提醒']]]]/following-sibling::div \
                                       //button[span[text()='返回']]")
    re.click()


def impstu(driver):
    pass


if __name__ == '__main__':
    self = startup
    startup(self)
    login(self)
    menu(self)
    newclass(self)
    gl1 = globalvar()
    cla = gl1.get_name()
    print(cla)
    queryclass(self, **cla)
    sleep(3)
    selectcla(self)
    notice(self)
