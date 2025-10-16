def max_sub_array(nums):
    cur_sum = max_sum = nums[0]
    for n in nums[1:]:
        if cur_sum < 0:
            cur_sum = n
        else:
            cur_sum += n

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

# --------------------------------------------------
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = max_sub_array(nums)
print(result)
