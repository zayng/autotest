#-*- coding:utf-8 -*-
'''
Created on 2015年11月13日

@author: 119937
'''
classfile=open('classname.dat','r')
for line in classfile:
    data=line.strip()    
    print(data,)
classfile.close()