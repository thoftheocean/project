import random
user_name = input('请输入你的名字：')
with open('guess_number.txt', 'w', encoding='utf-8')as f:
    f.write('')
num_time = 1
while True:
    # 用户输入数据
    start = input('请输入数字的范围，起始数字：')
    end = input('请输入数字的范围，结束数字：')
    guess_number = input("请输入所猜数字：")
    # 异常处理，主要提醒用户输入数字
    try:
        # 判定用户是否所猜数字是否在范围内
        if int(start) <= int(guess_number) <= int(end):
            with open('guess_number.txt', 'a', encoding='utf-8')as f:
                user_information = "第{}次猜测，用户姓名：{}，数字范围从{}到{}，猜测的数字：{}".format(num_time, user_name, start, end,
                                                                               guess_number)
                f.write(user_information + '\n')
            system_random = random.uniform(int(start), int(end))
            system_random = int(system_random)
            num_time += 1
            # 判定猜数是否成功
            if system_random != int(guess_number):
                print('系统猜测数字：%s' % system_random)
                print("猜数失败，虽然我这一次与你擦肩而过，请继续加油")
                # 判定用户失败后是否继续猜数
                print('亲，如果你现在想退出，我也不留你了')
                user_exit = input('请输入exit或者quit退出，否则按enter键继续:')
                if user_exit == 'exit' or user_exit == 'quit':
                    break
                else:
                    continue
            else:
                print('系统猜测数字：%s' % system_random)
                print('猜数成功，我们的缘分终于到了,恭喜你')
                break
        else:
            print('所猜数字不在范围，你想干嘛')
            continue
    except:

        print("你说你笨不笨，一定要输入数字哦")


