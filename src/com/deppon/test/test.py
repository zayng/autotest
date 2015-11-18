#-*- coding:utf-8 -*-
'''
Created on 2015年11月3日

@author: 119937
'''
import time
import datetime
import os 
classinfo={}
ts1=time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(ts1)

ts=datetime.datetime.today()
classinfo['ts']=ts
print(classinfo)

ts2=time.strftime('%y-%m-%d %H:%M:%S')
print(ts2)

print(os.path.abspath('..\\bin'))

cm=os.path.abspath('..\\bin')
print(cm)

# import random
# import shelve
# import sys
# print(sys.getdefaultencoding())
#print("//div[@id='T_authinfo-authClassMng']//tr[%s]/td[5]"%(ls))
# claNa=u"2015年%s期高级认证开班"%random.randint(1,2000)
# print(claNa)
# newclass=shelve.open('newclass.dat')
# newclass.write(claNa)
# newclass.close()
# 
# year,month,day=(2015,11,2)
# print(u"//td[@onclick='day_Click(%s,%s,%s);']"%(year,month,day))