def insertionSort(arr):
    for i in range(1, len(arr)):

        j = i
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


arr = [1, 2, 2, 3, 3, 6, 7, 8]

insertionSort(arr)
print(arr)