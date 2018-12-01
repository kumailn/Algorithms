def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
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