# You are given an array of integers a and two integers l and r.
# You task is to calculate a boolean array b,
# where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x
# and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

def solution(arr, left, right):
    resArray = []

    for i in range(0, len(arr)):
        isValid = False
        for x in range(left, right + 1):
            if arr[i] == (i + 1) * x:
                # resArray.append(True)
                isValid = True
                break
        # if not isValid:
        #     resArray.append(False)
        # isValid = False
        resArray.append(isValid)
    return resArray


arr = [1, 2, 3, 4, 5]
left = 1
right = 1
print(solution(arr, left, right))
