#Question: Given a sentence of words, find the shortest distance between two given words
#Difficulty: Easy
#Solution: Keep two pointers and the distance, update distance when the pointers are closer together
#Space Complexity: O(1)
#Time Complexity: O(n)

from typing import List

def shortestDistance(words: List[str], word1: str, word2: str) -> int:
  #Initialize two pointers, initialize distance to MAX_INTs
  p1 = p2 = -1
  distance = float('inf')

  #Loop through the words
  for i, v in enumerate(words):

    #Every time the current word is word1 update p1 and vice versa for p2
    if v == word1: p1 = i
    if v == word2: p2 = i

    #If we've found both word1 and word2 (ie when both pointers are not -1) 
    #Update distance to be the min or itself or the updated pointers
    if p1 != -1 and p2 != -1: distance = min(distance, abs(p1 - p2))
  return distance

def main():
  print(shortestDistance(["a","c","a","b"], "b", "a"))

main()