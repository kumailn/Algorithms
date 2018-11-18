#Question: Given a set of coins to chose from, and a target amount, find the number of different combinations you can have to make that amount 
#Solution: Dynamic Programming solution (DP)
#Difficulty: Medium

def coinChange(amount, coins):
    #Create a memoized store of the counts of combinations of the previous amount
    store = [0] * (amount + 1)
    #Let the count of combinations that sum to 0 be 1 (Since only no coins can sum to 0)
    store[0] = 1
    #For each coin in coins
    for coin in coins:
        #For each amount in the store
        for j in range(len(store)):
            #If the amount is greater than the coin in hand then increment the amount by the combinations that're at the amount which is this current amount - the coins value 
            if(j >= coin): store[j] += store[j-coin]
    print(store)
    return store[-1]


print(coinChange(3, [1, 2]))