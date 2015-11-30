#-*- coding:utf-8 -*-
'''
Created on 2015年11月30日

@author: 119937
'''
import hashlib
def encryp(pwd):
    dat=list('012345678qwertyuiopasdfghjklzxcvbnm')
    npwd=list(pwd)
    for m2 in npwd:
        if isinstance(m2,int):
            pass
    
if __name__=='__main__':
    dat=encryp('qqq1qqq')
    print(dat)