# 4.从排序的数组里面，删除重复的元素。重复的数字最多只能出现2次。nums=[1,1,1,2,2,3]，要求返回nums=[1,1,2,2,3]。
from collections import Counter
nums = [1, 1, 1, 2, 2, 3]
print(Counter(nums))
for k,v in Counter(nums).items():
    print(k,v)
    # if v > 2:
    #     nums.remove(k)
# print(nums)
