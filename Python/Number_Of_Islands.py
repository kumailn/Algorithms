#Question: Given a grid of 1s and 0s, determine the number of disjoint islands present if islands are connected by 1s
#Solution: Run a DFS on each island, making what you have covered
#Difficulty: Easy

def numIslands(self, grid):
        c = 0
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0": return
            grid[i][j] = "0"
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)
        for i, v in enumerate(grid):
            for j, u in enumerate(v):
                if u == "1": c += 1; dfs(i, j, grid)
        return c