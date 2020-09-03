import pandas as pd

test = pd.read_excel('e:/test.xlsx', index_col= '序号')
test.sort_values(by=['折扣','单价'], inplace=True, ascending=[False, True])
print(test)
