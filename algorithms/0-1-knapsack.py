def zeroOneKnapsack(items, capacity, index = 0, memo = None):
    if memo == None: memo = {}
    
    if index == len(items):
        return 0
    
    if capacity <= 0:
        return 0
    

    if index in memo and capacity in memo[index]:
        return memo[index][capacity]


    pick = items[index]["profit"] + zeroOneKnapsack(items, capacity - items[index]["weight"], index + 1, memo)
    skip = zeroOneKnapsack(items, capacity, index + 1, memo)

    if index not in memo:
        memo[index] = {}
    
    memo[index][capacity] = max(pick, skip)
    print(memo)
    return max(pick, skip)


capacity = 15
items = [
    {"weight": 1, "profit": 1},
    {"weight": 1, "profit": 3},
    {"weight": 5, "profit": 5},
    {"weight": 4, "profit": 6},
    {"weight": 9, "profit": 9},
]

maxProfit = zeroOneKnapsack(items, capacity)

print(maxProfit)