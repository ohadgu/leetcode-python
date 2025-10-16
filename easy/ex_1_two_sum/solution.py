def two_sum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        delta = target - num
        if delta in nums_dict:
            return nums_dict[delta], i
        nums_dict[num] = i
    else:
        return -1, -1


# nums = [2,7,11,15, 3]
# target = 10
nums, target = [-1, 2, 3, 4], 3
ids = two_sum(nums, target)
print(ids)
input("end")