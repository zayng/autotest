#-*- coding:utf-8 -*-
'''
Created on 2015年11月14日

@author: 119937
'''
import xlwt,xlrd
from  datetime import date,datetime

def read_excl():
    workbook=xlrd.open_workbook(r'demo.xlsx') 
    print(workbook.sheet_names())

if __name__=='__main__':
    read_excl()

