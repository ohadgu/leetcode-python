def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        delta = nums[mid] - target

        if delta == 0:
            return mid
        elif delta > 0:
            right = mid
        else:
            left = mid
    return -1

# ----------------------------------------------
nums = [-1,0,3,5,9,12]
target = 9
index = binary_search(nums, target)
print(index)