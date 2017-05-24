# usr/bin/env python
# encoding:utf-8
# hexi

'''
请使用面向对的方法,编写出双色球.
要求:按照双色球开奖规则.将每次开奖的双色球保存到本地的txt文档里面,
并双色球后面跟上日期.(提示,可能使用到库,random,time,os,sys等)
'''
import random
import time

class Ball:
    def __init__(self, num=1, color='red'):
        self.num = num
        self.color = color

    @staticmethod
    def get_num(color):
        if color == 'red':
            num = random.randint(1, 33)
        elif color == 'blue':
            num = random.randint(1, 16)
        else:
            print('颜色错误')
        return str(num)

class Write:
    @staticmethod
    def write_red_ball():
        str1 = str()
        for i in range(0, 6):
            str1 += Ball.get_num('red')+' '
        return str1

    @staticmethod
    def write_blue_ball():
        str2 = str()
        str2 += Ball.get_num('blue')
        return str2

    @staticmethod
    def write_time():
        now_time = time.localtime()
        myear = now_time.tm_year
        mmon = now_time.tm_mon
        mday = now_time.tm_mday
        now_time = str(myear)+'/'+str(mmon)+'/'+str(mday)
        return now_time

    def write_txt(self):
        with open('double_color_ball.txt', 'a+', encoding='utf-8')as f:
            f.write('红色号码:' + Write.write_red_ball() + ' 蓝色号码:' + Write.write_blue_ball() +' 日期:'+ Write.write_time() + '\n')
        with open('double_color_ball.txt', 'r+', encoding='utf-8')as f:
            print(f.read())

if __name__ == '__main__':
    ball1 = Ball()
    write = Write()
    write.write_txt()





















