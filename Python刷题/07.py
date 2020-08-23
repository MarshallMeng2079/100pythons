# 使用math库提供的函数（具体自己去查阅哦~）
#
# 将键盘输入的角度值转换为弧度值
#
# 将键盘输入的弧度值转换为角度值
import math

def trans_hd(a):
    return math.radians(a)

def trans_jd(b):
    return math.degrees(b)

if __name__ == '__main__':
    a = int(input("请输入a的角度值："))
    b = int(input("请输入b的弧度值："))
    print("a角度值%.2f的弧度值为%.2f" % (a, trans_hd(a)))
    print("b弧度值%.2f的角度值为%.2f" % (b, trans_jd(b)))
