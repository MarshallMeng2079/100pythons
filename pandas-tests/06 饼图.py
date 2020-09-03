import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
test = pd.read_excel('e:/test.xlsx', index_col='项目')
print(test)
# test['10月'].sort_values(ascending=True).plot.pie(fontsize=8,startangle=-270)
test['10月'].plot.pie(fontsize=8,counterclock=False,startangle=90)
plt.title('test',fontsize=20,fontweight='bold')
plt.show()