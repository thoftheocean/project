# !/usr/bin/env python
# encoding:utf-8
# author:hx

'''
请实现一个学生的类，有学号，有姓名，有年龄，以及成绩（100分），
并且实现一个公有的对象方法，get_level()，如果学员成绩大于等于80，
则返回“优等生”，小于80大于等于60，则返回“中等生”，小于60，则返回“差等生”

'''
#实例方法
#静态方法


class StudentMange():


    @staticmethod
    def get_info():

        #访问数据库
        return "班级1"

    @staticmethod
    def add():

        # 访问数据库
        return "班级1"

    @staticmethod
    def update():

        # 访问数据库
        return "班级1"

    @classmethod
    def get_student(cls, name, stu_num,  age, score):
        return cls( name, stu_num,  age, score)


    def __init__(self, name, stu_num,  age, score):
        self.name = name
        self.stu_num = stu_num
        self.age = age
        self.score = score
        self.grade = ''

    def get_level(self):
        if self.score >= 80:
            self.grade = self.name+'优等'
        elif 60 <= self.score < 80:
            self.grade = self.name+'中等'
        else:
            self.grade = self.name+'差等'

        return self.grade

if __name__ == '__main__':
    student1 = Student('张三', '123456789', 21, 89)
    print(student1.get_level())

    Student.get_student('张三', '123456789', 21, 89)
    print(student1.get_level())
