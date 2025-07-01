
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        if not (R and C):
            return 0
        
        counter = 0
        visited = [[0]*C for _ in range(R)]
        DIRS = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        
        def dfs(x, y):
            if not (0 <= x < R and 0 <= y < C):
                return
            
            if visited[x][y] == 1 or grid[x][y] == "0":
                return
            
            visited[x][y] = 1
            for i, j in DIRS:
                nx, ny = x + i, y + j
                dfs(nx, ny)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    counter += 1
                    dfs(i, j)
                    
        return counter
                        
        
        
        
        























class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        if not (R and C):
            return 0
        visted = [[False]*C for _ in range(R)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(x, y):
            if not ( 0 <= x < R and 0 <= y < C):
                return
            
            if visted[x][y] or grid[x][y] == "0":
                return
            
            visted[x][y] = 1
            for i, j in DIRS:
                nx, ny = x + i, y + j
                dfs(nx, ny)

        counter = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and not visted[i][j]:
                    counter += 1
                    dfs(i, j)
        return counter
        
        
        























