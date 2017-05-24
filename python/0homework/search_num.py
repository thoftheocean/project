# !/usr/bin/env python
# coding:utf-8
# author:hx
'''
实现一个函数handler_num,输入为一个任意字符串，请将字符串中的数
字取出，将偶数放入一个列表，再将奇数放入一个列表，并将两个列表返回
'''
str = raw_input('输入一串字符：')
def search_num(str):
    even = list()
    odd = list()
    result1 = dict()
    for i in str:
        if i.isdigit():
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        else:
            continue
    result1['even'] = even
    result1['odd'] = odd
    return result1
print search_num(str)




