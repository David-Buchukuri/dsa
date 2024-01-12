def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def partition(arr, left, right):
    lesserOrEqualElemsTillIdx = left
    pivot = arr[right]

    for i in range(left, right + 1):
        if arr[i] <= pivot:
            swap(arr, i, lesserOrEqualElemsTillIdx)
            lesserOrEqualElemsTillIdx += 1
    
    return lesserOrEqualElemsTillIdx - 1


def topK(arr, k):
    if k >= len(arr):
        return arr.copy()
    
    if k <= 0:
        return []

    left = 0
    right = len(arr) - 1
    pivotIdx = len(arr)
    targetPivotIdx = len(arr) - k

    while pivotIdx != targetPivotIdx:

        pivotIdx = partition(arr, left, right)

        if pivotIdx < targetPivotIdx:
            left = pivotIdx + 1
        else:
            right = pivotIdx - 1

    
    topK = []
    for i in range(targetPivotIdx, len(arr)):
        topK.append(arr[i])
    
    return topK


arr = [4, 6, 2, 3, 2]

result = topK(arr, 2)


print(result)