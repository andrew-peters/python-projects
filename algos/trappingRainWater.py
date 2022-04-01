def trap(heightArr):
    if not heightArr:
        return 0
    res = 0
    l, r = 0, len(heightArr) - 1
    lMax, rMax = heightArr[l], heightArr[r]
    while l < r:
        if lMax < rMax:
            l += 1
            lMax = max(lMax, heightArr[l])
            res += lMax - heightArr[l]
        else:
            r -= 1
            rMax = max(rMax, heightArr[r])
            res += rMax - heightArr[r]
    return res 

heightArr = [0, 1, 0, 0, 3, 2, 1, 0, 8, 0, 0, 0, 5]
print(trap(heightArr))