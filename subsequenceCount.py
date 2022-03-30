def solution(arr, queries):
    i = 0
    j = 0

    count = 0
    total_counts = []

    for query in queries:
        while i < len(query) and j < len(arr):
            if query[i] == arr[j]:
                i += 1
            j += 1
            if i == len(query):
                count += 1
                i = 0  # to reset i for query
        total_counts.append(count)
        count = 0

    return total_counts


queries = [[1, 1, 2], [1, 2, 1]]
arr = [1, 2, 2, 1, 2, 1, 2]
print(solution(arr, queries))
