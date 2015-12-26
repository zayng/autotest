class globalvar():
    classrec={}
    classdat=[]
    def set_name(self,ids,classname,li,le,ts):
        self.classrec['id']=ids
        self.classrec['name']=classname
        self.classrec['li']=li
        self.classrec['le']=le
        self.classrec['ts']=ts
        self.classdat.append(self.classrec)
        
    def get_name(self):
        return self.classdat[-1]
    def get_names(self):
        return self.classdat
    def get_class(self):
        return self.classrec

if __name__=='__main__':
    ran,name, li, le, sysdate=(2324,'中国上海32333',2,3,'2015-11-18')
    ran1,name1, li1, le1, sysdate1=(232422,'德邦物流优先公司',3,5,'2016-11-18')
    gl=globalvar()
    gl.set_name(ran,name, li, le, sysdate)
    gl.set_name(ran1,name1, li1, le1, sysdate1)
    gl1=globalvar()
    gl2=globalvar()
#     print(gl.get_name())
    print(gl1.get_name())
    print(gl2.get_name())
    print(gl1.get_names())