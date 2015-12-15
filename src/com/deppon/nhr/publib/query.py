#-*- coding:utf-8 -*-
'''
Created on 2015年11月9日

@author: 119937
'''

from time import sleep
import os
def readdat():
    filedat=os.path.abspath(r'..\bin\class-name.dat')
    with open(filedat) as file:
        readlins=[line.strip().split('#') for line in file.readlines()]
    return readlins

def queryclass(driver,li=1,le=1,*name):
    
    ''' 
            查询班级列表    
    li:认证大类
    le:认证层级   
    name:班级名称
    '''
    #输入班级名称
    clname=driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='classname']")
    clname.clear()
    clname.send_keys(name)
    sleep(1)
    #点击认证大类选择框
    #clakind=driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']/descendant::td[label[text()='认证大类:']]/following-sibling::td//td[2]")
    #clakind.click()
    driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='identificationkind']").click()
    #选择认证大类
    classli=driver.find_elements_by_xpath("//ul[count(li)>=13]/li[%s]"%li).pop()
    classli.click()
    
    #选择认证层级下拉框
    driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//input[@name='classlevel']").click()
    #选择认证层级
    classle=driver.find_elements_by_xpath("//ul[count(li)=4]/li[%s]"%le).pop()
    classle.click()
    sleep(1)
    #点击查询
    query=driver.find_element_by_xpath("//div[@id='T_authinfo-authClassMng']//button[span[text()='查询']]")
    query.click()
    
    
def selectcla(driver,se=1,*name):
    '''选择显示列表中的班级'''
    sleep(3)
    authlist=driver.find_elements_by_xpath("//div[@id='T_authinfo-authClassMng']//tbody/tr[count(td)=14]")
    if len(authlist)==1:
        authlist.pop().click()
    else:
        authlist.pop(se).click()
#     cNam=driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//div[text()='%s']"%classname)
#     cNam.click()    

def queryjudges(driver,*empcode):
    '''查询评委工号'''
    #清空收件人
    clearCode=driver.find_elements_by_xpath("//button[span[text()='清空收件人']]")
    clearCode.pop().click()
    
    #填写部门名称
#     dept=driver.find_elements_by_xpath("//input[@name='dept']")
#     dept.pop().send_keys("FOSS")
    for emp in range(len(empcode)):
        #按工号查询
        psn=driver.find_elements_by_xpath("//input[@name='number']")
        p=psn.pop()
        p.clear()
        print(empcode[emp])
        p.send_keys(empcode[emp])
        
        #点击查询
        queryBtn="//div[contains(@id,'button') and @style='border-width: 1px; left: 293px; margin: 0px; top: 0px; width: 75px;']//button[span[text()='查询']]"
        query=driver.find_elements_by_xpath(queryBtn)
        print(u"查询按钮的元素个数：%s"%len(query))
        query.pop().click()
        
        sleep(2)
        #选择工号
        psncode=driver.find_elements_by_xpath("//tr[count(td)=10]/td[1]")
        psncode.pop().click()
#         for code in psncode[-10:]:
#             code.click()
        #点击确定
        confirmstr=u"//div[em[button[span[text()='清空收件人']]]]/preceding-sibling::div//button[span[text()='确定']]"
        confirm=driver.find_elements_by_xpath(confirmstr)
        confirm.pop().click()
        
    #点击关闭按钮
    close=driver.find_elements_by_xpath("//button[span[text()='关闭']]")
    print(u"关闭按钮的元素个数:%s"%len(close))
    close.pop().click()
 
if __name__=='__main__':
    file=readdat()
    cla=file.pop()
    print(cla)