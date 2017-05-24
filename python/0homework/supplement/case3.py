# !/usr/bin/env python
# coding:utf-8
# author hx
'''
描述：
给了一串数字（不是扣扣号码），根据下面规则可以找出扣扣号码：首先删除第一个数
，紧接着将第二个数放到这串数字的末尾，再将第三个数删除，并将第四个数放到这串数字的末尾......如此循环，
知道剩下最后一个数，将最后一个数也删除，按照刚才删除的顺序，把这些数字连在一起就是女神的扣扣号码啦。
比如给一串数字：218916754
'''



# while i <= 7:
#     str1 += str[0]
#     print str1
#     str_new = str[2:]+str[1]
#     print str_new
#     if len(str_new)==2:
#         str1+=str_new[0]
#         str1 += str_new[1]
#         break
#     str = str_new
#     i+=1
# print str1

# #case1
# str='218916754'
# str1=''
# while len(str)>2:
#     str_new=str[2:]+str[1]
#
#     str1 +=str[0]
#     str =str_new
# str1 += str_new
# print str1

# #case2
# str='21891675'
# str1 = ''
#     str2 = ''
# while len(str)>=2:
#
#     for i in range(0,len(str)):
#         if i%2==1:
#             str1+=str[i]
#         else:
#             str2+=str[i]
#     str=str2
# print str1