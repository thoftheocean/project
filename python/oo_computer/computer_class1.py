# !/usr/bin/env python
# coding:utf-8
# author:hx

'''
# 请实现一个电脑的类，分别主机类、显示器类、鼠标类组成，
# 主机类、显示器类、鼠标类分别有品牌和价格的公有属性，
# 主机类有电源，显示器有分辨率，鼠标有有线或无线的特有属性，
# 请实现电脑类的两个公有对象方法，一个可以获得电脑的总价格，一个显示电脑配置的函数。
#“我的显示器是xx品牌，主机是xx品牌，”
# 要求，主机类、显示器类、鼠标类和键盘类要使用继承的方法。
'''

#共有属性类
class Device:
    def __init__(self, price, brand):
        self.__price = price
        self.__brand = brand

    def get_price(self):
        return self.__price

    def get_brand(self):
        return self.__brand
#主机类
class Host(Device):
    def __init__(self, brand, price, power):
        super().__int__(brand, price)
        self.__power = power

#显示器类
class Display(Device):
    def __int__(self, brand, price,  resolution):
        super().__init__(brand, price)
        self.__resolution = resolution
#鼠标类
class Mouse(Device):
    def __int__(self, brand, price, link):
        super().__init__(brand, price)
        self.__link = link

#电脑类
class Computer():
    def __init__(self):
        self.myprice = None
        self.mybrand = None

    def c_price(self, host, display, mouse):
        self.myprice = host_price + display_price + mouse_price
        return '电脑的总价格：' + str(self.myprice)

    def c_configuration(self, host_brand, display_brand, mouse_price):
        self.mybrand = '我的主机是'+host_brand+'我的显示器是' + display_brand + '我的鼠标是'+mouse_price
        return self.mybrand

if __name__ == '__main__':
    c_host = Host(100, 'sanxing')
    c_display = Display(20, 'huipu')
    c_mouse = Mouse(56, 'weiru')
    computer = Computer()
    print(computer.c_price(c_host.price, c_display.price, c_mouse.price))
    print(computer.c_configuration(c_host.brand, c_display.brand, c_mouse.brand))
