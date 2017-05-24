user_name = input('请输入你的名字：')
num_time = 1
while num_time <= 5:
    guess_number = input("请输入所猜数字：")
    start = input('请输入数字的范围,起始数字：')
    end = input('请输入数字的范围，结束数字')

    with open('record.txt','a',encoding='utf-8')as f:
        user_information = '第'+str(num_time)+'次猜测'+'\n'+'用户姓名：'+user_name+'\n'+'数字范围：'+start+'到'+end+'\n'+'猜测数字：'+guess_number
        f.write(user_information+'\n')

    import random
    start = int(start)
    end = int(end)
    system_random = random.uniform(start,end)
    system_random = int(system_random)
    # system_random // = 1
    num_time += 1

    if system_random != int(guess_number):
        print('系统猜测数字：%s' % system_random)
        print("猜数失败，请继续：")
        user_exit = input('不继续猜数请输入exit或者quit退出，否则按enter键退出:')
        if user_exit == 'exit' or user_exit == 'quit':
            exit()
            continue
    else:
        print('猜数成功')
        exit()
print("对不起，已经5次没有猜测成功了,请重新开始")
