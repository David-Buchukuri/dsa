def unboundedKnapsack(items, capacity, memo = None):
    if memo == None: memo = {}
    
    if capacity in memo:
        return memo[capacity]

    result = 0

    for item in items:
        if item["weight"] > capacity:
            continue

        result = max(
            result,
            item["profit"] + unboundedKnapsack(items, capacity - item["weight"], memo)
        )
    
    memo[capacity] = result
    return result



capacity = 500
items = [
    {"weight": 1, "profit": 1},
    {"weight": 1, "profit": 3},
    {"weight": 5, "profit": 5},
    {"weight": 4, "profit": 6},
    {"weight": 9, "profit": 9},
]

result = unboundedKnapsack(items, capacity)
print(result)

