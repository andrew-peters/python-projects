def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    nums.sort()
    print(nums)
    while l <= r:
        # m = l + ((r - l) // 2) -> if asked about overflow, this solves it
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


nums = [1, 3, 5, 9, 3, 2, 7, 1, -3, 20]
print(binarySearch(nums, 5))

