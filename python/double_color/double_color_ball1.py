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
        return num

class Write(Ball):
    def __init__(self, ball):
        super().__init__(self)
        self.ball = ball

    def write_red_ball(self):
        with open('double_color_ball.txt', 'a+', encoding='utf-8')as f:
            f.write('红色球号码:')
        for i in range(0, 6):
            with open('double_color_ball.txt', 'a+', encoding='utf-8')as f:
                f.write(str(self.ball.get_num('red'))+' ')

    def write_blue_ball(self):
        with open('double_color_ball.txt', 'a+', encoding='utf-8')as f:
            f.write('蓝色球号码：' + str(self.ball.get_num('blue'))+' ')

    def write_time(self):
        now_time = time.localtime()
        myear = now_time.tm_year
        mmon = now_time.tm_mon
        mday = now_time.tm_mday
        now_time = str(myear)+'/'+str(mmon)+'/'+str(mday)
        with open('double_color_ball.txt', 'a+', encoding='utf-8')as f:
            f.write('日期：'+now_time + '\n')
        with open('double_color_ball.txt', 'r+', encoding='utf-8')as f:
            print(f.read())

if __name__ == '__main__':
    ball1 = Ball()
    write = Write(ball1)
    write.write_red_ball()
    write.write_blue_ball()
    write.write_time()




















