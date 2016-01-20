# -*- coding:utf-8 -*-
"""
Created on '2016/1/15'

@author: '119937'
"""

from random import randint


allNums = []

for eachNum in range(9):
    allNums.append(randint(1, 99))
print(list(filter(lambda n: n % 2, allNums)))

m = map((lambda x: x+2), [0, 1 , 2, 3 , 4, 5])
print(list(m))