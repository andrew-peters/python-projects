# new arr b is arr a rearranged as such:
# b[0] = a[0]
# b[1] = a[last]
# b[2] = a[1]
# b[3] = a[last - 1]
# b[4] = a[2]
# and so on
# determin if new arr b is sorted in ascending order

def solution(a):
    b = []
    left = 0
    right = len(a) - 1
    numa, numb = 0, 0
    
    for i in range(len(a)):
        if i == 0:
            numa = a[0]
            left += 1
        if i % 2 == 0:
            numa = a[i//2]
            left += 1
        if i % 2 != 0:
            numa = a[right]
            right -= 1
        b.append(numa)
    print(b)
    return arraySortedOrNot(b)
    
def arraySortedOrNot(arr):
    n = len(arr)
    # Array has one or no element
    if (n == 0 or n == 1):
        return True
    for i in range(1, n):
        # Unsorted pair found
        if (arr[i-1] > arr[i]):
            return False
    # No unsorted pair found
    return True
            