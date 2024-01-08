def merge(arr1, arr2):
    merged = []

    idx1 = 0
    idx2 = 0

    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] < arr2[idx2]:
            merged.append(arr1[idx1])
            idx1 += 1
        else:
            merged.append(arr2[idx2])
            idx2 += 1
    
    while idx1 < len(arr1):
        merged.append(arr1[idx1])
        idx1 += 1

    while idx2 < len(arr2):
        merged.append(arr2[idx2])
        idx2 += 1
    
    return merged


def mergeSort(arr, left = None, right = None):
    if not arr: return []
    if left == None: left = 0
    if right == None: right = len(arr) - 1

    if left == right:
        return [arr[left]]
    
    middle = left + (right - left) // 2

    res1 = mergeSort(arr, left, middle)
    res2 = mergeSort(arr, middle + 1, right)

    return merge(res1, res2)

arr = [1, 5, 7, 3, 2, 12, 45, 650,-32, 2]

result = mergeSort(arr)

print(result)