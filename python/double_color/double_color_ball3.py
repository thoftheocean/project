# -*- coding: utf-8 -*-

import random
import time

class Ball(object):
    @staticmethod
    def get_random_num(min, max):
        return random.randint(min, max)

    @classmethod
    def create_red_ball(cls):
        ball = cls('red')
        ball.set_number(Ball.get_random_num(1, 36))
        return ball

    @classmethod
    def create_blue_ball(cls):
        ball = cls('blue')
        ball.set_number(Ball.get_random_num(1, 16))
        return ball

    def __init__(self, color):
        self.__color = color
        self.__nummber = 0

    def set_number(self, number):
        self.__nummber = number

    def get_number(self):
        return self.__nummber

    def get_color(self):
        return self.__color

def get_time():
    return time.strftime("%Y-%m-%d", time.localtime())


ball_list = []
for i in range(0, 6):
    red_ball = Ball.create_red_ball()
    print(red_ball.get_color(), red_ball.get_number())
    ball_list.append(red_ball)

blue_ball = Ball.create_blue_ball()
ball_list.append(blue_ball)
print(blue_ball.get_color(), blue_ball.get_number())

with open("reward.txt", "a") as f:
    i = 1
    for ball in ball_list:
        if i < 7:
            f.write(str(ball.get_number()) + "  ")
        elif i == 7:
            f.write('篮色号码:'+str(ball.get_number()) + "  ")
            f.write(get_time() + "\n")
        else:
            break
        i += 1


