from typing import  List
from collections import Counter

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0]) 
        
        DIRS = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        
        for i in range(R):
            for j in range(C):
                counter = Counter()
                for dx, dy in DIRS:
                    nx, ny = dx + i, dy + j
                    if 0 <= nx < R and 0 <= ny < C:
                        pass_vall = board[nx][ny]
                        if type(pass_vall) == tuple:
                            pass_vall = pass_vall[0]
                            
                        counter[pass_vall] += 1
                
                curr_val = board[i][j]
                next_val = 0
                if curr_val == 0:
                    if counter[1] == 3:
                        next_val = 1
                else:
                    if 2 <= counter[1] <= 3:
                        next_val = 1
                
                board[i][j] = (curr_val, next_val)
        
        for x in range(R):
            for y in range(C):
                _, one = board[x][y]
                board[x][y] = one
        
        return board
        
        
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        R, C = len(board), len(board[0])
        DIRS = [(-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1)]

        # --- faza 1: oblicz nowy stan i zapisz go w 2. bicie ---
        for r in range(R):
            for c in range(C):
                live = 0
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        live += board[nr][nc] & 1   # TYLKO stary bit
                if board[r][c] & 1:                 # komórka była żywa
                    if 2 <= live <= 3:
                        board[r][c] |= 2            # pozostanie żywa
                else:                               # była martwa
                    if live == 3:
                        board[r][c] |= 2            # ożyje

        # --- faza 2: uaktualnij planszę ---
        for r in range(R):
            for c in range(C):
                board[r][c] >>= 1                   # nowy bit → bit 0
