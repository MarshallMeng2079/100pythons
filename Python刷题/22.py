# 暂停一秒输出。
import time
import os

for i in range(10):
    print(10-i)
    time.sleep(1)
    if 10-i == 5:
        time.sleep(2)

