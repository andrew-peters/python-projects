def twoSum(self, nums: List[int], target: int) -> List[int]:
    compliments = {}

    for i in range(len(nums)):
        num = nums[i]
        if num in compliments:
            return [compliments[num], i]

        if num not in compliments:
            compliments[target - num] = i
    
    return []