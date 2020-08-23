# 输入某年某月某日，判断这一天是这一年的第几天？
import datetime

def day(y,m,d):
    x_new = datetime.date(y,m,d)
    x_std = datetime.date(y,1,1)
    return x_new.__sub__(x_std)

if __name__ == '__main__':
    y = int(input("请输入年:"))
    m = int(input("请输入月:"))
    d = int(input("请输入日:"))
    print(day(y,m,d))