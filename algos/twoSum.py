def twoSum(nums, target):
    compliments = {}

    for i in range(len(nums)):
        num = nums[i]
        if num in compliments:
            return [compliments[num], i]

        if num not in compliments:
            compliments[target - num] = i
    
    return []