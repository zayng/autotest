#-*- coding:utf-8 -*-
'''
Created on 2015年11月17日

@author: 119937
'''
from com.deppon.nhr.login.login import nhrLogin
from com.deppon.nhr.publib.calendar import calendar
from com.deppon.nhr.login.authclass import newclass
from com.deppon.nhr.student import impstudent
from com.deppon.nhr.publib.query import queryclass,readdat
from time import sleep

auth=nhrLogin()
auth.login()
auth.menu()
driver=auth.driver
try:
    count=0
    for li in range(1,3):
        for le in range(1,5):
            name=newclass(driver,li,le)
            queryclass(driver,li,le,name)
            sleep(2)
    print("总计新增班级成功:%s"%count)
finally:  
    auth.logout()
