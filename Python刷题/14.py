# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

l = [1,2,3,4]
for i in l:
    for j in l:
        for k in l:
            if i == j or i == k or j == k:
                continue
            else:
                print(int(str(i)+str(j)+str(k)))

