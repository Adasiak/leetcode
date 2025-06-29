from collections import deque
from typing import List


class Solution:
    minutes = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        # visited = [[0] * c for _ in range(r)]
        
        def bfs(x, y):
            # if visited[x][y] == 1:
            #     return
            # visited[x][y] = 1
            
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if grid[x][y] == 2:
                for i, j in dirs:
                    if (0 <= x + i < r and 0 <= y + j < c ):
                        if grid[x + i][y + j] == 1:
                            grid[x + i][y + j] = 2
                            bfs(x + i, y + j)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    bfs(i, j)        
        return self.minutes if 1 not in grid else -1
    
    
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        R, C = len(grid), len(grid[0])
        q = deque()                          # KOLEJKA (x, y, minute)
        fresh = 0                            # licznik świeżych
        latest = 0  
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, minute = q.popleft()
            latest = max(latest, minute)
            for i, j in dirs:
                nx, ny = x + i, y + j
                if (0 <= nx < R and 0 <= ny < C ):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny, minute + 1))
                        fresh -= 1
        return latest if not fresh else -1
    
    
      
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        latest = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q:
            x, y, minute = q.popleft()
            latest = max(minute, latest)
            
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, j in dirs:
                nx, ny = x + i, y + j
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny, minute + 1))
                        fresh -= 1
        return -1 if fresh else latest
        
        


