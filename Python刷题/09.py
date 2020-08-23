# 从键盘输入要求和的浮点数个数n（n不超过10）
#
# 然后依次从键盘输入n个浮点数
#
# 使用列表存储这些数
#
# 使用math中的fsum对这些浮点数求和
import math
l = []
while len(l)<10:
    num = float(input('输入浮点数：'))
    l.append(num)

print(math.fsum(l))