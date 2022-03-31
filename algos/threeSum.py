def threeSum(self, nums):	
    res = set()  
    visitedLeft = set()
    visitedRight = set()
    
    for lIdx, lVal in enumerate(nums):  
        if lVal not in visitedLeft:
            visitedLeft.add(lVal) 
            visitedRight.clear() 
            for midRightVal in nums[lIdx+1:]: 
                midValToCheck = 0-lVal-midRightVal 
                if midValToCheck in visitedRight: # If we've seen it in the middle, we just found the right value
                    tup = tuple(sorted((lVal, midValToCheck, midRightVal)))
                    res.add(tup)    
                visitedRight.add(midRightVal) # Remember that we've seen this middle value
            
    return res