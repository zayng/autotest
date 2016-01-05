#-*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
def  is_prame(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % 2 == 0:
            return False
    return True

if __name__=='__main__':
    print(is_prame(2))