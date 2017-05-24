from tkinter import*
import tkinter.simpledialog as dl
import tkinter.messagebox as mb
import random
#设置GUI
root = Tk()
w = Label(root, text='猜数字游戏')
w.pack()

#欢迎消息
mb.showinfo('欢迎', '欢迎来到猜数字游戏')
#定义范围变量
low = 1
height = 100

# 生成随机数
number = random.randint(low, height)
while True:
    #用户输入信息
    guess = dl.askinteger('Number', '猜数范围1到100，输入你的猜测数字')
    if guess < 1 or guess > 100:
        output = '亲，你走错片场了吧！输入的数字不在范围内'
        mb.showinfo('Hint:', output)
    elif guess == number:
        output = '恭喜，猜数正确'
        mb.showinfo('欢迎来到数字竞猜游戏:', output)
        break
    elif guess < number:
        low = guess
        output = '猜测数字比系统小，新范围'+str(low)+'--' + str(height)
        low = guess
        mb.showinfo('欢迎来到数字竞猜游戏', output)
    else:
        height = guess
        output = '猜测数字比系统大，新范围' + str(low)+'--' + str(height)
        mb.showinfo('欢迎来到数字竞猜游戏', output)
print('结束')

