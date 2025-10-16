def contains_duplicate(nums):
    nums_set = set()
    for n in nums:
        if n in nums_set:
            return True
        nums_set.add(n)
    return False