# Question(#1143): Given two strings text1 and text2, return the length of their longest common subsequence.
# Solution: Use the longest common susequence dynamic programming algorithm

def longestCommonSubsequence(text1: str, text2: str) -> int:
    grid = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
    
    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                grid[i][j] = 1 + grid[i-1][j-1]
            else:   
                grid[i][j] = max(grid[i][j-1], grid[i-1][j])

    return grid[-1][-1]