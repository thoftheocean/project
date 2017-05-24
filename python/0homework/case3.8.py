#coding: utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: hexi
#输入一行字符，判定字母、数字、空格和其他字符的个数

var = input("请输入一行字符：")
alpha_count = 0
digit_count = 0
space_count = 0
other_count = 0
for i in var:
    if i.isalpha():
        alpha_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1
    else:
        other_count += 1
print("字母%s个,数字%s个,空格%s个,其他字符%s个" % (alpha_count, digit_count, space_count, other_count))

