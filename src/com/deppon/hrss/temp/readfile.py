#-*- coding:utf-8 -*-
'''
Created on 2015年11月13日

@author: 119937
'''
classfile=open('classname.dat','r')
data=[line.strip() for line in classfile]    
print(data.pop(),)
classfile.close()