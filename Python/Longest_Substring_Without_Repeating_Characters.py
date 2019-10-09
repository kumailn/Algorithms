# Question: Given a string find the largest substring that consists of only unique characters
# Solution: Store the last seen position of letters in a hashmap
# Difficulty: Medium 

def lengthOfLongestSubstring(s: str) -> int:
    # We initialize each letter to -1 indicating we haven't seen it yet
    lastSeen = {v: -1 for v in s}
    
    # We start from -1 to handle the edge case where the string has length 1
    # because if length was one we woule compute longest as i - start (0 - 0) and return 0
    # instead of returning 1
    start, longest = -1, 0

    for i, v in enumerate(s):
        
        # If the letter was seen after the starting index of our current
        # index, then set the new start to be the letter 
        start = max(start, lastSeen[v])
        lastSeen[v] = i
        longest = max(longest, i - start)
    return longest
