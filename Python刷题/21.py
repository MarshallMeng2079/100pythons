# 输出 9*9 乘法口诀表。
for a in range(1,10):
    print()
    for b in range(1,a+1):
        print("%d * %d = %d" %(b,a,a*b), end='\t')