# -*- coding:utf-8 -*-
"""
Created on '2016/1/18'

@author: '119937'
"""
from selenium import webdriver
from com.deppon.hrpr.pages.login import LoginNHR
from com.deppon.hrpr.pages.newclass import AddClassName
from com.deppon.hrpr.pages.queryclass import QueryClass
from com.deppon.hrpr.pages.selectclass import SelectClass
from com.deppon.hrpr.pages.newstudent import ImpStudent
from com.deppon.hrpr.pages.newtask import AddTask

driver = webdriver.Firefox()
# 登录NHR
login = LoginNHR(driver)
login.user_login()
# # 新增班级
# add = AddClassName(driver)
# add.add_newclass_page()
# 查询选拔认证班级
query = QueryClass(driver)
query.queryclass_page(**{'large': 2, 'level': 1})
# query.queryclass_page(**{'classname': '2015年第7163期认证开班', 'large': 1, 'level': 1})
# 选择选拔认证班级
setup = SelectClass(driver)
setup.select_authlist_page()
# setup.save_classinfo()
# 导入认证选拔学员名单
# imp = ImpStudent(driver)
# imp.imp_student_page()
# 添加评委
task = AddTask(driver)
task.add_task_page()
