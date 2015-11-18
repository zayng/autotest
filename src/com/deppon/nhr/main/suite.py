#-*- coding:utf-8 -*-
'''
Created on 2015年11月17日

@author: 119937
'''
from com.deppon.nhr.login.login import nhrLogin
from com.deppon.nhr.login.authclass import newclass
from com.deppon.nhr.student.impstudent import notice,selectcla
from com.deppon.nhr.publib.query import queryclass,queryjudges
from time import sleep
from com.deppon.nhr.globalvar import globalvar
from com.deppon.nhr.judges.task import task

auth=nhrLogin()
auth.login()
auth.menu()
driver=auth.driver
try:
    count=0
    for li in range(1,3):
        for le in range(1,5):
            newclass(driver,li,le)
            gl=globalvar()
            name=gl.get_name()
            queryclass(driver,li,le,name)
            selectcla(driver)
            notice(driver)
#             selectcla(driver)
#             task(driver)
            count+=1
            sleep(2)
    print("总计新增班级成功:%s"%count)
finally:  
    auth.logout()
