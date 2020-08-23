# 使用random中的randint函数随机生成一个1~100之间的预设整数
#
# 让用户键盘输入所猜的数，如果大于预设的数，屏幕显示“太大了，请重新输入”
#
# 如果小于预设的数，屏幕显示“太小了，请重新输入”
#
# 如此循环，直到猜中，显示“恭喜你，猜中了！共猜了N次”N为用户猜测次数

import random
num = random.randint(1,100)
i = 1
while True:
    user = int(input("请输入数字"))
    if user > num:
        print("太大了，请重新输入")
        i +=1
    elif user < num:
        print("太小了，请重新输入")
        i +=1
    else:
        print("恭喜你，猜中了！共猜了%d次" %i)
        break
