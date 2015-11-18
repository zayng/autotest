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

  

def identification(driver,li,le):
    '''新增开班，选择认证大类和层级 '''

    print("选择认证大类")
    #点击认证大类下拉选择框
    ciIdenti=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='identificationkind']")
    ciIdenti.click()

    #选择具体大类//body/div[contains(@id,'boundlist')]//li[text()='IT类']
    seLarge=driver.find_element_by_xpath("//ul[count(li)=13]/li[%s]"%li)
    seLarge.click()
    
    print("选择认证层级")
    #点击认证层级下拉选择框
    ciLeve=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classlevel']")
    ciLeve.click()
    
    #选择层级
    seLeve=driver.find_element_by_xpath("//ul[count(li)=4]/li[%s]"%le)
    seLeve.click()
    
    if le in [1,2,3]:
        #专业笔试成绩
        writtenratio=driver.find_element_by_name("writtenratio")
        writtenratio.clear()
        if li in range(4,7):
            writtenratio.send_keys(0)
        else:
            writtenratio.send_keys(20)        
    elif le == 4:
        #专业影响力
        majorratio=driver.find_element_by_name("majorratio")
        majorratio.clear()
        majorratio.send_keys(10)
    else:
        print("选择认证层级参数错误")

def newclass(driver,li=3,le=2):
    ''' 在班级列表，点击新增按钮添加新班级'''
    #生成标示符号
    classinfo={}
    ran=random.randint(1,9999)
    #新增开班
    classbtn=driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()='新开班']]")
    classbtn.click()
    
    #输入开班名称
    name=u"2015年第%r期认证开班"%(ran)
    print(name)
    classNa=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='classname']")
    classNa.send_keys(name)
    
    #输入地点
    addr=u"德邦学院D%r"%random.randint(100,200)
    print(addr)
    address=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//input[@name='address']")
    address.send_keys(addr)
    
    #选择认证类型与认证层级
    identification(driver,li,le)
    
    print("选择开始时间")
    #选择开始时间
    newBegin=driver.find_element_by_xpath(u"//td[@id='newClassbegintime-inputCell']/following-sibling::td/div[1]")
    newBegin.click()
    #调用时间控件选择开始时间
    calendar(driver,fg=0)
    
    #选择结束时间
    newEnd=driver.find_element_by_xpath(u"//td[@id='newClassendtime-inputCell']/following-sibling::td/div[1]")
    newEnd.click()
    
    #调用时间控件选择开始时间
    calendar(driver,23,30,20,yy=2015,mm=11,dd=30,fg=1)
      
    #保存新开班级
    saClass=driver.find_element_by_xpath(u"//body/div[contains(@id,'ext-comp')]//button[span[text()='确定']]")
    saClass.click()
    sleep(4)
    #获取提示信息，如果保存成功，保存班级名称
    message=u"//div[contains(@id,'messagebox')]//div[contains(text(),'保存成功！')]"
    msg=WebDriverWait(driver,10).until(ex.text_to_be_present_in_element((By.XPATH,message),u'保存成功'))
     
    #确定保存
    print("保存新增班级")
#     rk=driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]")
#     rk.click()
    rk=u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]"
    element=WebDriverWait(driver,10).until(ex.presence_of_element_located((By.XPATH,rk)))
    sysdate=strftime('%Y-%m-%d %X')
    element.click()
    classinfo['id']=ran
    classinfo['name']=name
    classinfo['li']=li
    classinfo['le']=le
    classinfo['ts']=sysdate
    clalist=[name,li,le,sysdate]
    print(classinfo)
    #存储新增班级名称

    if msg:
        print("保存新增班级到dat文件")
        filename=os.path.abspath(r'..\bin\class-name.dat')
        filecsv=os.path.abspath(r'..\bin\class-table.csv')
        file=open(filename,'a')
        file.write("%s#%s#%s#"%(name,li,le))
        file.write(sysdate)
#         file.write('#'.join(clalist))
        file.write('\n')
        file.close()
        print("保存新增班级到CSV文件")
        with open(filecsv,'w',newline='') as csvfile:
            fieldnames=['id','name','li','le','ts']
            writer=csv.DictWriter(csvfile,fieldnames)
            writer.writeheader()
            writer.writerow(classinfo)
    return name       
if __name__=="__main__":
    auth=nhrLogin()
    auth.login()
    auth.menu()
    driver=auth.driver
    try:
        count=0
        for li in range(1,3):
            for le in range(1,5):
                newclass(driver,li,le)
                count+=1
        print("总计新增班级成功:%s"%count)
    finally:  
        auth.logout()
