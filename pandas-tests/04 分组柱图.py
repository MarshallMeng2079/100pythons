import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
test = pd.read_excel("e:/汇总表.xlsx")
print(test)
test.plot.bar(x='分公司系统工会', y=['2019年实际计拨工会经费总额（元）', '2019年实际上缴总公司系统工会经费总额（元）'], color=['orange', 'red'])
plt.title('测试表', fontsize=16, fontweight='bold')
plt.xlabel('系统工会', fontsize=14, fontweight='bold')
plt.ylabel('经费', fontsize=14, fontweight='bold')
ax = plt.gca()
ax.set_xticklabels(test['分公司系统工会'], rotation=45, ha='right')
f = plt.gcf()
f.subplots_adjust(left=0.2,bottom=0.42)
# plt.tight_layout()
plt.show()
