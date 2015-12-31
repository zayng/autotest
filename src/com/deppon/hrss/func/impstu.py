"""
Created on 2015年11月3日

@author: 119937
"""

from time import sleep
import os

from com.deppon.hrss.publ.log4 import log

from com.deppon.hrss.func.authcla import newclass
from com.deppon.hrss.globalvar import globalvar
from com.deppon.hrss.publ.query import queryclass, selectcla
from com.deppon.hrss.func.login import startup, login, menu

def notice(self, stufile="../temp/stuAuthImport.xlsx"):
    """导入学员
    :param stufile:导入学员模板的路径
    :param self:
    :return:无
    """
    log.info("导入学员")
    driver = self.driver
    impfile = os.path.abspath(stufile)

    # 点击学员通知按钮
    notified = driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()"
                                            u"='学员通知']]")
    notified.click()
    '''
    # 使用调用au3程序导入学员模板
    driver.find_element_by_xpath(u"//button[span[text()='浏览']]").click()
    # 调用uoloadfile.exe上传文件
    sleep(1)
    bin_home = os.path.abspath('../temp/uploadfile.exe')
    os.system(bin_home)
    # os.system("../temp/uploadfile.exe")
    '''
    # 将导入学员模板excel路径输入到浏览按钮
    log.info("导入学员模板路径：%s" % os.path.abspath(stufile))
    driver.find_element_by_xpath("//input[@name='stuexcel']").send_keys(impfile)

    # 点击导入按钮
    driver.find_element_by_xpath(u"//button[span[text()='导入']]").click()
    sleep(2)

    # 导入成功
    driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]").click()
    log.info("导入学员成功，返回班级列表")
    # 返回班级列表
    re = driver.find_element_by_xpath(u"//div[em[button[span[text()='邮件提醒']]]]/following-sibling::div \
                                       //button[span[text()='返回']]")
    re.click()

if __name__ == '__main__':
    self = startup
    startup(self)
    login(self)
    menu(self)
    newclass(self)
    gl1 = globalvar()
    cla = gl1.get_name()
    queryclass(self, **cla)
    selectcla(self)
    notice(self)
