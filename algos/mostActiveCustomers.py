# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
# return the list of customers whose occurences
# make up at least 5% of the total number of customers
from collections import Counter

def mostActive(customers):
    n = len(customers)
    res =[]
    custSet = Counter(customers)
    for val in custSet:
        
        if custSet[val] / n >= .05:
            res.append(val)
    res.sort()
    return res

customers = ["andrew", "andrew", "andrew", "madi", "cust", "madi", "madi", "madi", "madi",  "cust"]
print(mostActive(customers))