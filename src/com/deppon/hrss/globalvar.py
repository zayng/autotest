def globalvar(*vargs):
    classdat=[]
    for item in vargs:
        classdat.append(item)
    return classdat


if __name__=='__main__':
    ran,name, li, le, sysdate=(2324,'中国上海3333',2,3,2015-11-18)
    gl=globalvar(tuple('asoidhoasid'))
    print(gl)