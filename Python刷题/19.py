# 斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# def fblist(x):
#     y = l[x - 3] + l[x - 2]
#     return y
#
# if __name__ == '__main__':
#     x = int(input("请输入一个整数(>=3)："))
#     f0 = 0
#     f1 = 1
#     l = [f0, f1]
#     while len(l) < x:
#         l.append(fblist(len(l)+1))
#     print(l)

def fib(x):
    fibs = [0, 1]
    if x <=2:
        return fibs[0:x]
    else:
        for i in range(2,x):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

if __name__ == '__main__':
    x = int(input("请输入一个正整数："))
    print(fib(x))


