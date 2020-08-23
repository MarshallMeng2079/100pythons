# 从键盘中输入两个数a，b，求他们的四则运算结果，要求保留两位小数。

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def times(a,b):
    return a*b

def div(a,b):
    return a/b


if __name__ == '__main__':
    a = int(input("请输入a的数字："))
    b = int(input("请输入b的数字："))
    print("a+b=%.2f" %add(a, b))
    print("a-b=%.2f" %sub(a, b))
    print("a*b=%.2f" %times(a, b))
    print("a/b=%.2f" %div(a, b))


