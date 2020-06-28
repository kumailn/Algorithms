// Question: Given a list of stock prices each day, determine the most profit you could make buying and selling the stock once
// Solution: Loop through finding the minimum price each time, and then the max profit. This works because the profit will be negative on days where the stock goes down
// Difficulty: Easy
// Time Complexity: O(n)
// Space Complexity: O(n)

import "math"

func maxProfit(prices []int) int {
    lowestPrice := math.Inf(1)
    maxProfit := float64(0)
    
    for _, v := range prices {
		// Update lowestPrice to be the min found so far, and maxProfit to the max profit if we solf the lowestPrice today
		// this works because lowestPrice is always in the past and maxProfit is calculated for today
        lowestPrice = math.Min(lowestPrice, float64(v))
        maxProfit = math.Max(maxProfit, float64(v) - lowestPrice)
    }
    
    return int(maxProfit)
}