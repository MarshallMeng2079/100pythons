import pandas as pd

test = pd.read_excel("e:/test.xlsx")
df = test['NAME'].str.split(expand=True)
test['A'] = df[0]
test['B'] = df[1]
print(test)