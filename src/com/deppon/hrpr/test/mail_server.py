# -*- coding:utf-8 -*-
"""
Created on '2016/1/26'

@author: '119937'
"""
import smtplib
from smtplib import SMTPException

from email.mime.text import MIMEText

sender = 'zhouyang014@deppon.com'
receivers = ['zhouyang014@deppon.com', 'gaoli005@deppon.com']

mailobj = smtplib.SMTP('client.deppon.com', '25')
message = """From:test
To:test,test2
Subject:test

    This is test e-mail.
"""
try:
    msg = MIMEText(message, _subtype='plain', _charset='utf-8')
    mailobj.sendmail(sender, receivers, msg.as_string())
    print("发送邮件成功！")
except SMTPException:
    print("Error:unable to send email")
