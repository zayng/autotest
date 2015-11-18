#-*- coding:utf-8 -*-
'''
Created on 2015年11月18日

@author: 119937
'''
class globalvar():
    classrec={}
    name=[]
    def set_name(self,ids,name,li,le,ts):
        self.name.append(name)
        self.classrec['id']=ids
        self.classrec['name']=name
        self.classrec['li']=li
        self.classrec['le']=le
        self.classrec['ts']=ts
    def get_name(self):
        return self.name.pop()
    
    def get_class(self):
        return self.classrec

if __name__=='__main__':
    ran,name, li, le, sysdate=(2324,'中国上海3333',2,3,2015-11-18)
    gl=globalvar()
    gl.set_name(ran,name, li, le, sysdate)
    c=gl.get_name()
    d=gl.get_class()
    print(c,d)