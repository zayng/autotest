# -*- coding:utf-8 -*-
"""
Created on '2016/1/26'

@author: '119937'
"""
import smtplib
from smtplib import SMTPException

sender = 'zhouyang014@deppon.com'
receivers = ['zhouyang014@deppon.com', 'gaoli005@deppon.com']

mailobj = smtplib.SMTP('client.deppon.com', '25')
message = """
From:测试人员
To:test,test2
Subject:测试主题

    This is test e-mail.
"""
try:
    mailobj.sendmail(sender, receivers, message)
    print("发送邮件成功！")
except SMTPException:
    print("Error:unable to send email")
