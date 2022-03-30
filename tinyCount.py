def solution(a, b, k):
    tinyCnt = 0
    n = len(a) - 1
    for i in range(len(a)):
        num = int(str(a[i]) + str(b[n]))
        if num < k:
            tinyCnt += 1
        n -= 1
    return tinyCnt