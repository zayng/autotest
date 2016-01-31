# -*- coding:utf-8 -*-
"""
Created on '2016/1/27'

@author: '119937'
"""
from tqdm import tqdm
from time import sleep

for i in tqdm(range(1, 20)):
    sleep(1)
else:
    print("下载完毕")