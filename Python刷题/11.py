# 使用python的格式化输出方式输出如下图形
#
# 代码力求简洁
# 20*10
# row = 1\10\20
a = '+'
b = '-'
c = '|'
d = ' '
for i in range(1, 12):
    if i in [1, 6, 11]:
        print(a, b * 4, a, b * 4, a)
    else:
        print(c, d * 4, c, d * 4, c)


# for row in range(1, 12):
#     for col in range(1, 20):
#         if row in [1,6,11]:
#             if col in [1,10]:
#                 print(a,end="")
#             elif col == 19:
#                 print(a)
#             else:
#                 print(b,end="")
#         else:
#             if col ==1 or col == 10:
#                 print(c,end="")
#             elif col == 19:
#                 print(c)
#             else:
#                 print(" ",end="")
