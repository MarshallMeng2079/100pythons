# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
test = pd.read_excel("e:/test.xlsx")
test.sort_values(by='数量', inplace=True, ascending=False)
print(test)
# test.plot.bar(x='项目', y='数量',color='orange')
plt.bar(test.数量, test.项目, color='orange')
plt.xticks(test.数量, rotation='90')
plt.xlabel('项目')
plt.ylabel('数量')
plt.title('测试数据表', fontsize=16)
plt.show()