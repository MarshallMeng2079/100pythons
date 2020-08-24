# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""
2,2,4,6,10,16,26...
"""



def rabbits_sum(time):
    r_1 = 2
    r_2 = 2
    if time <= 2:
        return 2
    else:
        for i in range(time-3):
            r_1 += r_2
            r_2 += r_1
        if time % 2 == 0:
            return r_2
        else:
            return r_1


if __name__ == '__main__':
    time = int(input("输入第几个月："))
    print(rabbits_sum(time))
