def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    len_original = len(nums)
    left = 0
    right = len(nums)
    nums = [n for n in nums if n != 0]
    len_new = len(nums)
    for _ in range(len_original - len_new):
        nums.append(0)

nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0,