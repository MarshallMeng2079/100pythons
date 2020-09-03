import pandas as pd


name = pd.read_excel("e:/test.xlsx", sheet_name='Sheet1', index_col='ID')
score = pd.read_excel("e:/test.xlsx", sheet_name='Sheet2', index_col='ID')
# print(name)
# print(score)
table = name.join(score, how='left').fillna(0)
# table = name.merge(score, how='left', on='ID').fillna(0)
table.SCORE = table.SCORE.astype(int)
print(table)