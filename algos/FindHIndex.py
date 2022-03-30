def hIndex(citations):
    citations.sort()
    n = len(citations)
    h = n
    while h > 0:
        print("is", citations[n - h], ">=", h, "?")
        if citations[n - h] >= h:
            print("Yes, we done fam")
            return h
        print("nah, try again")
        h -= 1
    return 0

inArray = [1, 7, 9, 4]
inArray2 = [8, 5, 3, 2, 1, 9, 10, 2, 2, 8, 5, 7, 20]
print("The H index is:",hIndex(inArray2))

