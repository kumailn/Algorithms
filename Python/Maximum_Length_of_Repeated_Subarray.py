# Question(#718): Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
# Solution: Use the longest common substring algorithm and optimize it to use only O(N) space
# Difficulty: Medium

def findLength(A: List[int], B: List[int]) -> int:
    # Keep track of the last row of each letter
    last = [0 for _ in range(len(B)+1)]
    maxlen = 0

    for i in range(1, len(A)+1):
        # Current represents the current row, we only really need two rows at any given time to compute our solution
        current = [0 for _ in range(len(A)+1)]
        for j in range(1, len(B)+1):
            # If the elements are equal then the longest subarray must be the longest subarray we see if we remove both elements 
            # for example [1, 2, 3] and [0, 2, 3], if we're at index 2 in each array then the longest subarray if both elements at index 2
            # are the same is the longest subarray at index 1. 
            if A[i-1] == B[j-1]:
                current[j] = 1 + last[j-1]
                # Keep track of the max since we might lose it as we're clearing our current row each time
                maxlen = max(maxlen, current[j])
        last = current
    return maxlen