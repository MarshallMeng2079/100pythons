import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
test = pd.read_excel('e:/test.xlsx')
test['合计'] = test['10月'] + test['11月'] + test['12月']
test.sort_values(by='合计', inplace=True, ascending=True)
print(test)
test.plot.barh(x='项目', y=['10月', '11月', '12月'], stacked=True, title='测试表')
plt.tight_layout()
plt.show()
