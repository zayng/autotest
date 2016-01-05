#-*- coding:utf-8 -*-
'''
Created on 2015年11月3日

@author: 119937
'''
from com.deppon.nhr.login.login import nhrLogin
from com.deppon.nhr.publib.query import queryclass,selectcla
from time import sleep
import os
   
def  notice(driver):
    #点击学员通知按钮
    notified=driver.find_element_by_xpath(u"//div[@id='T_authinfo-authClassMng']//button[span[text()='学员通知']]")
    notified.click()
    
    #浏览文件路径，浏览
    driver.find_element_by_xpath(u"//button[span[text()='浏览']]").click()
    #调用uoloadfile.exe上传文件
    sleep(1)
    BIN_HOME=os.path.abspath(r'..\bin\uploadfile.exe')
    os.system(BIN_HOME)
    #os.system("D:\\119937\\workspace\\autotest\\src\\com\\deppon\\nhr\\bin\\uploadfile.exe")
     
    #浏览文件路径，input控件
#     inputfile=driver.find_element_by_xpath("//input[@name='']")
#     inputfile.send_keys(u"d:\\119937\\Desktop\\data\\stuAuthImport.xlsx")
     
    #点击导入按钮
    driver.find_element_by_xpath(u"//button[span[text()='导入']]").click()
    sleep(2)

    #导入成功
    driver.find_element_by_xpath(u"//body/div[contains(@id,'messagebox')]//button[span[text()='确定']]").click()
    
    #返回班级列表
    re=driver.find_element_by_xpath(u"//div[em[button[span[text()='邮件提醒']]]]/following-sibling::div//button[span[text()='返回']]")
    re.click()
      
def impStu(driver):
    pass
    
if __name__=='__main__':
    st=nhrLogin()
    st.login()
    st.menu()
    driver=st.driver
    queryclass(driver)
    sleep(3)
    selectcla(driver, ls=6)
    notice(driver)
    