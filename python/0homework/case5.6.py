import time

try:
    # 读入文件
    with open('record.log', 'r', encoding='utf-8')as f:
        for i in f:
            print(f)
except :
    print('没有record.log文件')

try:
    # 2写入文件
    while True:
        line = input('输入你想要保存的信息：')
        # 得到系统时间
        if line == 'exit' or line == 'quit':
            break
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        with open('record.log', 'a', encoding='utf-8')as f1:
            f1.write(now+' '+line + '\n')
except :
    print("写入文件出错")

