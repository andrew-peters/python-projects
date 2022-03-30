def minCost(costs):
    resCost = 0
    for group in costs:
        minNum = min(group[0], group[1], group[2])
        resCost += minNum         

    return resCost 


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(minCost(costs))