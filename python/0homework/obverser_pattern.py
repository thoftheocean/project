# usr/bin/env python
# encoding:utf-8
# author:hexi

'''
项目一：观察者模式
观察者模式，又称发布订阅模式，是我们经常用的一个设计模式，
比如Django Signal就是观察者模式的应用。而在生活当中，
我们可以通过邮局订阅杂志或者报纸，出版社通过订阅信息主动向我们
邮寄订阅的杂志或者报纸，这就观察者模式在生活中的一个典型应用，
用Python和面向对象实现这一个场景的代码
'''
'''
分析
主题：订阅信息
观察者：用户和出版社
'''
# 抽象的观察者
class Obverser():
    def __init__(self, name):
        self.name = name

    def action(self):
        pass

# 具体的观察者
class Sub_obverser(Obverser):
    def action(self):
        print(self.name+'要订阅杂志或者报纸')

class Post_obverser(Obverser):
    def action(self):
        print(self.name+'快邮寄用户订阅的杂志或者报纸')

# 主题
class Sub_system():
    def __init__(self):
        self.obverser = []

    def add(self, new_obverser):
        self.obverser.append(new_obverser)

    def inform(self):
        for p in self.obverser:  # 2
            p.action()

if __name__ == '__main__':
    system = Sub_system()
    obverser1 = Sub_obverser('tom')
    obverser2 = Post_obverser('Post')
    system.add(obverser1)
    system.add(obverser2)
    system.inform()



