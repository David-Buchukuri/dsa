def swap(idx1, idx2, arr):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def cycleSort(arr):
    for i in range(len(arr)):
        if i == arr[i]:
            continue

        while i != arr[i]:
            swap(i, arr[i], arr)


arr = [5, 4, 9, 1, 6, 8, 7, 3, 2, 0]

cycleSort(arr)

print(arr)