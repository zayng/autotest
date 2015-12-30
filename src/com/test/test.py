# -*- coding:utf-8 -*-
'''
Created on 2015年12月2日

@author: 119937
'''
from com.test.count import count


class TestCount():
    def test_add(self):
        try:
            j = count(2, 4)
            add = j.add
            assert (add == 5), "Inter addtion result error"
        except AssertionError as msg:
            print(msg)
        else:
            print('test pass')


if __name__ == '__main__':
    test = TestCount()
    test.test_add()
