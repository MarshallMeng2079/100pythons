# 题目：判断101-200之间有多少个素数，并输出所有素数。

def su_num(a, b):
    l = []
    for i in range(a, b):
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1
        if j == i:
            l.append(i)
    return l


if __name__ == '__main__':
    print(su_num(2, 1000))
