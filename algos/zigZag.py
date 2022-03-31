def solution(numbers):
    resArr = []
    idx = 0
    length = len(numbers)
    while idx < length - 2:
        if numbers[idx + 1] > numbers[idx] and numbers[idx + 1] > numbers[idx + 2]:
            resArr.append(1)
        elif numbers[idx + 1] < numbers[idx] and numbers[idx + 1] < numbers[idx + 2]:
            resArr.append(1)
        else:
            resArr.append(0)
        idx += 1
    return resArr

    
nums = [1, 2, 1, 3, 1, 2, 3, 2, 3, 1]
print(solution(nums))