# 2.在一个数组里面移除指定的数字，并返回一个从大到小排序的新数组。比如:nums=[1，6，6，3，6，2，10，2，100]，remove_num=6，
# 要求返回时nums=[1，2，3，10，100]。


# remove_num = 6
# nums = [1,6,6,3,6,2,10,2,100]
# while remove_num in nums:
#     nums.remove(remove_num)
# print(sorted(nums, reverse=False))

remove_num = 6
nums = [1,6,6,3,6,2,10,2,100]
print(sorted(filter(lambda x: x != remove_num, nums), reverse=False))



