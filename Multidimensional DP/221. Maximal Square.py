from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        
        dp = [[0]*C for _ in range(R)]
        mm = 0
        
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0 or int(matrix[i][j]) == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = ( min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1],
                    ) + 1 ) 
                mm = max(mm, (dp[i][j])**2 )
        return mm
    
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        
        prev = [0]*(C+1)
        curr = [0]*(C+1)
        mm = 0
        
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if int(matrix[i - 1][j - 1]) == 1:
                    curr[j] = ( min(
                        prev[j - 1],
                        curr[j - 1],
                        prev[j],
                    ) + 1 ) 
                    mm = max(mm, (curr[j])**2 )
                else:
                    curr[j] = 0
            prev, curr = curr, prev
        return mm