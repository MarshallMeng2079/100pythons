import pandas as pd

test = pd.read_excel('e:/test.xlsx', index_col='序号')
test = test.loc[test['单价'].apply(lambda a : 4 <= a < 18)].loc[test.折扣.apply(lambda a : a == 0.8)]
print(test)