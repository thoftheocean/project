# coding=utf-8
# author hx

# 判定一个数是否为质数
def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('%s不是质数' % num)
                break
        else:
            print('%s是质数' % num)
    else:
        print('%s是质数' % num)
    return 