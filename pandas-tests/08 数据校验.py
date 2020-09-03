import pandas as pd

def data_check(row):
    # if not 5<=row.SCORE<=10:
    #     print("%s的分数%.1f有误" %(row.NAME, row.SCORE))
    try:
        assert 5<=row.SCORE<=10
    except:
        print("%s的分数%.1f有误" % (row.NAME, row.SCORE))


test = pd.read_excel('e:/test.xlsx')
test.apply(data_check, axis =1)

