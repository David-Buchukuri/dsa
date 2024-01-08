def countSort(arr):
    maxElem = max(arr)
    minElem = min(arr)
    numCounts = {}

    for num in arr:
        if num not in numCounts:
            numCounts[num] = 0
        numCounts[num] += 1
    
    result = []
    for num in range(minElem, maxElem + 1):
        if num not in numCounts:
            continue

        for _ in range(numCounts[num]):
            result.append(num)
    
    return result

arr = [1, 7, 4, 3, 5, 6, 5, 4, 3, 2, 6, 8, 9]
result = countSort(arr)
print(result)