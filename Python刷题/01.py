# 1.能被3或5整除的1000以内的数字和。
result = 0
for i in range(1000):
    if i % 3 ==0 or i % 5 ==0:
        result += i

print(result)