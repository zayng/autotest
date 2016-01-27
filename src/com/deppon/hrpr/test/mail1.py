# -*- coding:utf-8 -*-
"""
Created on '2016/1/26'

@author: '119937'
"""
import smtplib
from smtplib import SMTPException


sender = 'zhouyang014@deppon.com'
receivers = ['zhouyang014@deppon.com', 'gaoli005@deppon.com']


message = """From:From Person <zhouyang014@deppon.com>
To:To Person <zhouyang014@deppon.com>, gaoli <gaoli005@deppon.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail 测试邮件

    This is test e-mail.
    <b>This is HTML message.</b>
    <h1>This is headline.</h1>
"""
try:
    mailobj = smtplib.SMTP('client.deppon.com', '25')
    mailobj.sendmail(sender, receivers, message)
    print("Successfuly sent emial")
except SMTPException:
    print("Error:unable to send email")
