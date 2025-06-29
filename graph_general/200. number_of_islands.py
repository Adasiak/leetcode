from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        def dfs(r: int, c: int):
            # poza planszą
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # woda lub już odwiedzone
            if grid[r][c] == "0" or visited[r][c]:
                return
            visited[r][c] = True
            # 4 kierunki
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    count += 1      # nowa wyspa!
                    dfs(r, c)       # „zalewamy” całą wyspę
        return count
    
    
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    counter += 1
                    dfs(r, c)
        return counter
    


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        
        def dfs(r,c):
            if c < 0 or c >= cols or r < 0 or r >= rows or grid[r][c] == "0" or visited[r][c]:
                return
            visited[r][c] = True
            dfs(r - 1, c )
            dfs(r + 1, c )
            dfs(r , c - 1)
            dfs(r , c + 1)
            
        couter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    couter += 1
                    dfs(row, col)
        return couter