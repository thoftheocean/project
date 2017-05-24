# !/usr/bin/env python
# coding:utf-8
# author hx

#1请将字符串“1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn”中，[[]]中的字符取出来，并打印使用字符串操作！
# str1 = '1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn'
# alphabet = list()
# for i in str1:
#     if i.isalpha():
#         if i != 'm' and i != 'n':
#             alphabet.append(i)
#         else:
#             continue
#     else:
#         continue
# print alphabet

#2 请将字符串“1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn”中，[[]]中的字符取出来，并打印使用字符串操作！
# Str1 = input(str('请输入字符串：'))
# Str2 = input('目标字符1：')
# a = (Str1.find(Str2))
# print (a)
# print (Str1[a:a+len(Str2)])

#3 请将字符串“1234[[xyz]]5678[[abcd]]90[[ttkk]]mmnn”中，[[]]中的字符取出来，并打印使用字符串操作！
str1 = '1234[[xy]]5678[[abcd]]90[[ttkk]]mmnn'
str2 = '[['
str3 = ']]'
start = str1.find(str2)
end = str1.find(str3)
while start != -1 and end != -1:
    print(str1[start + 2:end])
    str1 = str1[end + 2:len(str1)]
    # print "str1:", str1
    start = str1.find(str2)
    end = str1.find(str3)





