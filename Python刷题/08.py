# 假设你在复习考研，一个月假设有30天，第一天你的刷题能力为1000
#
# 当你认真复习一天时，该天的刷题能力会比前一天提高5%
#
# 当你吃鸡或者王者荣耀玩一天时，该天的刷题能力会比前一天降低10%
#
# 如果你每天认真复习持续一个月，和你每天吃鸡或者王者荣耀持续一个月
#
# 一个月后两种状态的能力值相差多少
#
# 保留小数点后2位

c = 1000
t = 30
def study(c,t):
    return c * 1.05 ** (t-1)

def game(c,t):
    return c * 0.9 ** (t-1)

if __name__ == '__main__':
    print("刷题一个月，能力达到%.2f" %study(c,t))
    print("王者一个月，能力达到%.2f" %game(c,t))