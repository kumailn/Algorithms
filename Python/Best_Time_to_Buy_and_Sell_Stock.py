#Question: Given a list of stock prices each day, determine the most profit you could make buying and selling the stock once
#Solution: Loop through finding the minimum price each time, and then the max profit. This works because the profit will be negative on days where the stock goes down
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)

from typing import List

def maxProfit(prices: List[int]) -> int:
  #Initialize lowestPrice to MAX_INT and mostProfit to be 0 
  lowestPrice, mostProfit = float('inf'), 0

  for i, price in enumerate(prices):
      #In each loop determing the lowest price, and the max profit by subtracting the current price by the lowest known one 
      lowestPrice = min(lowestPrice, price)
      mostProfit = max(price - lowestPrice, mostProfit)
  return mostProfit

def main():
  print(maxProfit([7,1,5,3,6,4]))

main()
