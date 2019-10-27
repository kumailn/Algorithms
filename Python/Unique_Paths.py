# Question (#62): Given a grid, find the number paths there are that you can take to get to the last position 
# Solution: Use dynamic programming to build up the number of paths possible, the number of paths at each position 
#           in the grid is the sum of the number of paths possible to the grid above and the grid to the left
# Difficulty: Medium

def uniquePaths(m: int, n: int) -> int:
    # Set up an m by n grid, set all positions to 1 initially, since there's at least 1 way to get anywhere 
    grid = [[1] * n] * m

    # Start looping through rows and colums, start at 1 since we need to look 
    # to the left and top positions in the grid to find the number of paths 
    for i in range(1, m):
        for j in range(1, n):
            # Set each position in the grid to be the sum of the paths possible above it and to it's left
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    # Return the last position in the grid, as thats the total number of paths possible to get to the end of the grid 
    return grid[-1][-1]