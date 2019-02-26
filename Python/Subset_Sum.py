def subsetSum(nums, sumTo):
    sumleft = sumTo
    store = [[0 for i in range(sumTo + 1)] for j in range(len(nums) + 1)]
    print(store)

    for i in range(1, len(nums) + 1):
        for w in range(1, sumTo + 1):
            if w > sumleft:
                store[i][sumleft] = store[i - 1][w]
            else:
                store[i][sumleft] = max(store[i - 1][sumleft], w + store[i - 1][sumleft - w])
    print(store)
    return store[len(nums)][sumTo]

def main():
    print(subsetSum([3, 34, 4, 12, 5, 2], 9))

main()