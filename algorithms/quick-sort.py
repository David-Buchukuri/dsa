def swap(idx1, idx2, arr):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp


def partition(arr, left, right):
    pivot = arr[right]

    # left denote till which index are
    # elements less or equal to pivot located  

    for i in range(left, right + 1):
        if arr[i] <= pivot:
            swap(i, left, arr)
            left += 1

    return left - 1
    


def quickSort(arr, left = None, right = None):
    if left == None: left = 0
    if right == None: right = len(arr) - 1

    if left >= right:
        return
    
    pivotIdx = partition(arr, left, right)
    quickSort(arr, left, pivotIdx - 1)
    quickSort(arr, pivotIdx + 1, right)


arr = [1, 2, 9, 7, 4, 7, 4, 9, 4]

quickSort(arr)
print(arr)