#-*- coding:utf-8 -*-
'''
Created on 2015年11月30日

@author: 119937
'''
import hashlib
def encryp(pwd):
    dat=list('012345678qwertyuiopasdfghjklzxcvbnm')
    pwd=list(pwd)
    for m1,m2 in enumerate(pwd):
        if isinstance(m2,str):
            print(m1,m2)
#         print("m2",m1,m2)
if __name__=='__main__':
    dat=encryp('qqq1qqq')
    print(dat)