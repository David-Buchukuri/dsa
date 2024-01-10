def maximumSubArray(arr):
    maximum = float('-inf')
    curr = 0

    for num in arr:
        curr += num
        maximum = max(maximum, curr)
        curr = max(curr, 0)

    return maximum

arr = [-2, 1, -3, 4, -3, 3, 2, -5, 4]
result = maximumSubArray(arr)
print(result)

        

