def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    nums_idx_dict = {}
    for i, num in enumerate(nums):
        if (num in nums_idx_dict) and (abs(i - nums_idx_dict[num]) <= k):
                return True
        nums_idx_dict[num] = i
    return False