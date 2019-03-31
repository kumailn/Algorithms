// Question: Given a grid of 1s and 0s, determine the number of disjoint islands present if islands are connected by 1s
// Solution: Run a DFS on each island, making what you have covered
// Difficulty: Easy

int numIslands(char** grid, int gridRowSize, int gridColSize) {
    int count = 0;
    void dfs(int i, int j, char** grid) {
        if (i < 0 || j < 0 || i >= gridRowSize || j >= gridColSize || grid[i][j] == '0') return;
        grid[i][j] = '0';
        dfs(i - 1, j, grid);
        dfs(i + 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i, j - 1, grid);
    }
    
    for(int i = 0; i < gridRowSize; i++) {
        for (int j = 0; j < gridColSize; j++) { 
            if (grid[i][j] == '1') {
                count++;
                dfs(i, j, grid);
            } 
        }
    }
    
    return count;
}