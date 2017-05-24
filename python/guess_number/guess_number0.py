import random
user_name = input('请输入你的名字：')
num_time = 1
while num_time <= 5:
    # 用户输入数据
    guess_number = input("请输入所猜数字：")
    start = input('请输入数字的范围，起始数字：')
    end = input('请输入数字的范围，结束数字：')
    # 判定输入的猜测的数是否在范围内
    if int(start) <= int(guess_number) <= int(end):
        # 在文本中写入输入的数据
        with open('record1.txt', 'a', encoding='utf-8')as f:
            user_information = '第' + str(
                num_time) + '次猜测' + '\n' + '用户姓名：' + user_name + '\n' + '数字范围：' + start + '到' + end + '\n' + '猜测数字：' + guess_number
            f.write(user_information + '\n')

        system_random = random.uniform(int(start), int(end))
        system_random = int(system_random)
        # system_random // = 1
        num_time += 1
        # 判定猜数是否成功
        if system_random != int(guess_number):
            print('系统猜测数字：%s' % system_random)
            print("猜数失败，虽然我这一次与你擦肩而过，请继续加油")
            #判定用户失败后是否继续猜数
            print('亲，如果你现在想退出，我也不留你了')
            user_exit = input('请输入exit或者quit退出，否则按enter键继续:')
            if user_exit == 'exit' or user_exit == 'quit':
                exit()
                continue
        else:
            print('系统猜测数字：%s' % system_random)
            print('猜数成功，我们的缘分终于到了， Congratulations')
            exit()
    else:
        print('所猜数字不在范围，你想干嘛')
        continue
print("亲，你都猜了五次了,下次再来吧")
