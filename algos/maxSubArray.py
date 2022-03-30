from typing import List

def maxSubArray(nums):
        res, cur, subArray = nums[0], 0, []
        for n in nums:
            cur += n
            if cur > res:           
                res = cur
            if cur > 0:
                subArray.append(n)    
            if cur < 0:
                cur = 0
        return res, subArray

print(maxSubArray([-1, -9, 10, 10, -5, 8, 1, 0, -2, 8]))
