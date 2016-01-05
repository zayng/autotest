#-*- coding:utf-8 -*-
'''
Created on 2015年11月14日

@author: 119937
'''
import csv
 

# csv_file=open('test.csv','a',newline='')
# name=['Name','Sex','Blog']
# writer=csv.DictWriter(csv_file,fieldnames=name)
# writer.writeheader()
# d={}
# d['Name']='Qi'
# d['Sex']='周阳'
# d['Blog']='http//www.redicen.com'
#  
# writer.writerow(d)
# csv_file.close()
classinfo={'ts': '2015-11-14 10:13:58', 'le': 1000, 'li': 1, 'name': '2015年第8960期认证开班', 'id': 8960}
dat=list('oiadfhaopsnflasfniowhefoi')
with open('class-table1.csv','a+',newline='') as csvfile:
    writer=csv.writer(csvfile,dialect='excel')
    writer.writerow(dat)
    
# import csv
#  
# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#  
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
