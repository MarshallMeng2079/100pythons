import os
import pandas as pd

path = r'E:\分公司信息核对与收集表'
fl = os.listdir(path)

for i in fl:
    temp = pd.read_excel(path + '/' + i, header=2)
    # print(temp.head())
    i = i[8:-5]
    print(i)
    print(temp.loc[temp['所属分公司'].str.contains(i, na = False)])
    # print(temp)
    temp.to_excel('temp.xlsx')


