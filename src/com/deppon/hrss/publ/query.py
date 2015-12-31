# -*- coding:utf-8 -*-
'''
Created on 2015年11月9日

@author: 119937
'''

from time import sleep
import os

from com.deppon.hrss.publ.log4 import log


def readdat():
    filedat = os.path.abspath(r'..\temp\class-name.dat')
    with open(filedat) as file:
        readlines = [line.strip().split('#') for line in file.readlines()]
    return readlines


def queryclass(self, **name):
    """
    查询班级列表
    li:认证大类
    le:认证层级
    name:班级名称
    """
    driver = self.driver
    log.info("开始查询询班级")
    for key, value in name.items():
        print(key, "==>", value)

    if 'name' in name.keys():
        # 输入班级名称
        sleep(3)
        clname = driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='classname']")
        clname.clear()
        clname.send_keys(name['name'])
    sleep(3)
    driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='identificationkind']").click()
    # 选择认证大类
    classli = driver.find_elements_by_xpath("//ul[count(li)>=13]/li[%s+1]" % name['li']).pop()
    classli.click()
    # 选择认证层级下拉框
    driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='classlevel']").click()
    # 选择认证层级
    classle = driver.find_elements_by_xpath("//ul[count(li)=4]/li[%s+1]" % name['le']).pop()
    classle.click()
    sleep(1)
    # 点击查询
    query = driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//button[span[text()='查询']]")
    query.click()


def selectcla(self, se=0, *name):
    """选择显示列表中的班级
    :param driver:
    :param se:
    :param name:
    :return:
    """
    driver = self.driver
    sleep(3)
    authlist = driver.find_elements_by_xpath("//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]")
    if len(authlist) == 1:
        authlist.pop().click()
    else:
        authlist.pop(se).click()


def queryjudges(driver, *empcode):
    """
    查询评委工号
    """
    log.info("开始添加任务评委")
    # 清空收件人
    clearcode = driver.find_elements_by_xpath("//button[span[text()='清空收件人']]")
    clearcode.pop().click()

    # 填写部门名称
    #     dept=driver.find_elements_by_xpath("//input[@name='dept']")
    #     dept.pop().send_keys("FOSS")
    for emp in range(len(empcode)):
        # 按工号查询
        psn = driver.find_elements_by_xpath("//input[@name='number']")
        p = psn.pop()
        p.clear()
        print(empcode[emp])
        p.send_keys(empcode[emp])

        # 点击查询
        querybtn = "//div[contains(@id,'button') and @style='border-width: 1px; left: 293px; margin:" \
                   " 0px; top: 0px; width: 75px;']//button[span[text()='查询']]"
        query = driver.find_elements_by_xpath(querybtn)
        print(u"查询按钮的元素个数：%s" % len(query))
        query.pop().click()

        sleep(2)
        # 选择工号
        psncode = driver.find_elements_by_xpath("//tr[count(td)=10]/td[1]")
        psncode.pop().click()
        #         for code in psncode[-10:]:
        #             code.click()
        # 点击确定
        confirmstr = u"//div[em[button[span[text()='清空收件人']]]]/preceding-sibling::div//button[span[text()='确定']]"
        confirm = driver.find_elements_by_xpath(confirmstr)
        confirm.pop().click()
    log.info("评委添加成功")
    # 点击关闭按钮
    close = driver.find_elements_by_xpath("//button[span[text()='关闭']]")
    print(u"关闭按钮的元素个数:%s" % len(close))
    close.pop().click()


if __name__ == '__main__':
    file = readdat()
    cla = file.pop()
    print(cla)
