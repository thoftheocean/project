# def check_num(pernum):
#     sum = 0
#     i=1
#     while i < pernum:
#         if pernum % i == 0:
#             sum += i
#         i += 1
#     if sum == pernum:
#         print('Ture')
#     else:
#         print('False')
# check_num(8)

# 教程程序
def CheckNum(num):
    #求出数的因子
    list1=[]
    for i in range(1,num):
        if num % i == 0:
            list1.append(i)
    sum = 0
    for j in list1:
        sum += j
    if sum == num:
        return True
    else:
        return False
print(CheckNum(5))
print(CheckNum(6))



