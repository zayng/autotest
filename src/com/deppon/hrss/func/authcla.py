#-*- coding:utf-8 -*-
'''
Created on 2015年11月2日

@author: 119937
'''
from com.deppon.nhr.login.login import nhrLogin
from com.deppon.nhr.publib.calendar import calendar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from time import sleep,strftime
import random,csv,os

from com.deppon.hrss import categories,log,calendar


def newclass(driver,li=2,le=1):
    ''' 在班级列表，点击新增按钮添加新班级'''
    #生成标示符号
    ran=random.randint(1,9999)
    #新增开班
    log.info('点击新增开班')
    newClass_btn=driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]")
    newClass_btn.click()
    #输入开班名称
    log.info("使用随机函数random.randint,生成班级名称和地点")
    name=u"2015年第%r期认证开班"%(ran)
    log.info("班级名称生成成功，生成班级名称："+name)
    log.info("输入班级名称")
    classNa=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classname']")
    classNa.send_keys(name)
    
    #输入地点
    addr=u"德邦学院D%r"%random.randint(100,200)
    log.info("开班地点生成成功，生成地点名称："+addr)
    log.info("输入开班地址")
    address=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='address']")
    address.send_keys(addr)
    
    #选择认证类型与认证层级
    log.info("选择认证类型和认证层级，开始调用identification函数")
    
    categories(driver,li,le)
    
    log.info("选择班级开始时间和结束时间")
    #选择开始时间
    newBegin=driver.find_element_by_xpath(u"//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]")
    newBegin.click()
    
    #调用时间控件选择开始时间
    calendar(driver,fg=0)
    
    #选择结束时间
    newEnd=driver.find_element_by_xpath(u"//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]")
    newEnd.click()
    
    #调用时间控件选择结束时间
    calendar(driver,23,30,20,yy=2015,mm=12,dd=30,fg=1)
     
    log.info("开始保存新增班级.....")  
    #保存新开班级
    saClass=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
    saClass.click()
    sysdate=strftime('%Y-%m-%d %X')
    sleep(4)
    #获取提示信息，如果保存成功，保存班级名称
    message=u"//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
    msg=WebDriverWait(driver,10).until(ex.text_to_be_present_in_element((By.XPATH,message),u'保存成功'))
     
    #确定保存
    log.info("新增班级成功，新增班级名称："+name)
#     rk=driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]")
#     rk.click()
    rk=u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
    element=WebDriverWait(driver,10).until(ex.presence_of_element_located((By.XPATH,rk)))
    element.click()

    #存储新增班级名称
    if msg:
        log.info("保存新增班级到dat文件")
        filename=os.path.abspath(r'..\bin\class-name.dat')
        with open(filename,'a') as f:
            f.write("%s#%s#%s#%s\n"%(name,li,le,sysdate))
            
            
#if __name__=="__main__":
#     auth=nhrLogin()
#     auth.login()
#     auth.menu()
#     driver=auth.driver
#     try:
#         count=0
#         for li in range(13):
#             for le in range(4):
#                 log.info("创建新开班的认证和层级："+data(li,le))
#                 newclass(driver,li,le)
#                 log.info("保存班级信息到列表:"+str(data))
#                 count+=1
#                 log.info("已经累计新增班级：%d"%(count))
#     except Exception as e:
#         driver.quit()
#     finally:  
#         pass
# #         auth.logout()