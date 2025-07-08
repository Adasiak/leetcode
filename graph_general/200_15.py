from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        
        visited = [[False] * C for _ in range(R)]
        
        DIRS = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        def dfs(x, y):
            if visited[x][y] or int(grid[x][y]) == 0:
                return
            
            visited[x][y] = True
            for dx, dy  in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    dfs(nx, ny)
                    
        counter = 0
        for i in range(R):
            for j in range(C):
                if int(grid[i][j]) == 1 and not visited[i][j]:
                    dfs(i, j)
                    counter += 1
                    
        return counter