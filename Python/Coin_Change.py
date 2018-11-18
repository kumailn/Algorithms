#Question: Given a set of coins to chose from, and a target amount, find the number of different combinations you can have to make that amount 
#Solution: Dynamic Programming solution (DP)

# amount = total amount, coins = array of coin
def coinChange(amount, coins):
    store = [0] * (amount + 1)
    store[0] = 1
    for coin in coins:
        for j in range(len(store)):
            if(j >= coin):
                store[j] += store[j-coin]
    print(store)


print(coinChange(3, [1, 2]))