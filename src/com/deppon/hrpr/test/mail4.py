# -*- coding:utf-8 -*-
"""
Created on '2016/1/26'

@author: '119937'
"""
import smtplib
from smtplib import SMTPException
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8').encode(), addr)

from_addr = input("From:")
password = input("Password:")
to_addr = input("To:")
smtp_server = input("SMTP SERVER:")

msg = MIMEText('hello, send by python', _subtype='plain', _charset='utf-8')

msg['From'] = _format_addr("Python爱好者 <%s>" % from_addr)
msg['To'] = _format_addr("管理者 <%s>" % to_addr)
msg['Subject'] = Header("++++++++来自SMTP的测试邮件++++++", charset='utf-8').encode()

try:
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Successfuly sent emial")
except SMTPException:
    print("Error:unable to send email")
