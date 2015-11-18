#-*- coding:utf-8 -*-
'''
Created on 2015年11月17日

@author: 119937
'''
import csv
classinfo={'ts': '2015-11-14 10:13:58', 'le': 1000, 'li': 1, 'name': '2015年第8960期认证开班', 'id': 8960}

with open('class-dict.csv','w',newline='') as csvfile:
    fieldnames=['id','name','li','le','ts']
    writer=csv.DictWriter(csvfile,fieldnames)
    writer.writeheader()
    writer.writerow(classinfo)
    
with open('class-dict.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row['name'],row['id'])