# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

num = int(input("输入一个正整数："))
print("%d = " %num ,end="")
# num_l = []
for i in range(2, num):
    while num % i == 0:
        num = num / i
        if num != 1:
            print("%d" %i,end="*")
        else:
            print("%d" %i,end="")





