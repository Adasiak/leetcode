from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C = len(heights), len(heights[0])
        efforts = [[float("inf")] * (C) for _ in range(R)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)] # (aktualny maks-wysiłek, r, c)
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            curr, r, c = heappop(pq)
            if r == R - 1 and c == C - 1:
                return curr
            if curr > efforts[r][c]:
                continue
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    step = abs(heights[nr][nc] - heights[r][c])
                    next = max(curr, step)
                    if next < efforts[nr][nc]:
                        efforts[nr][nc] = next
                        heappush(pq, (next, nr, nc))
        return 0
    
    
    
    
    




class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        efforts = [[float("inf")] * C for _ in range(R)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            curr, x, y = heappop(pq)
            if x + 1 == R and y + 1 == C:
                return curr
            if curr > efforts[x][y]:
                continue
            for i, j in DIRS:
                nx, ny = x + i, y + j
                if 0 <= nx < R and 0 <= ny < C:
                    step = abs(heights[nx][ny] - heights[x][y])
                    next = max(curr, step) 
                    if next < efforts[nx][ny]:
                        efforts[nx][ny] = next
                        heappush(pq, (next, nx, ny))
        return 0
    
    
    
    
    
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        efforts = [[float("inf")]*C for _ in range(R)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        while pq:
            curr, x, y = heappop(pq)
            if x + 1 == R and y + 1 == C:
                return curr
            if curr > efforts[x][y]:
                continue
            
            for i, j in DIRS:
                nx, ny = x + i, y + j
                if 0 <= nx < R and 0 <= ny < C:
                    step = abs(heights[nx][ny] - heights[x][y])
                    next = max(curr, step)
                    if curr < efforts[nx][ny]:
                        efforts[nx][ny] = curr
                        heappush(pq, (next, nx, ny))
        return 0
    
    
    
   
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        effort = [[float("inf")] * (C) for _ in range(R)]
        effort[0][0] = 0
        
        pq = [(0, 0, 0)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            cur, x, y = heappop(pq)
            if x + 1 == R and y + 1 == C:
                return cur
            if cur > effort[x][y] :
                continue
        
            for i, j in DIRS:
                nx, ny = x + i, y + j
                if 0 <= nx < R and 0 <= ny < C:
                    step = abs(heights[nx][ny] - heights[x][y])
                    next = max(cur, step)
                    if cur < effort[nx][ny]:
                        effort[nx][ny] = cur
                        heappush(pq, (next, nx, ny))
            return 0