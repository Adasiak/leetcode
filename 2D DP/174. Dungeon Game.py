from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        dp = [[(1, 1)]*C for _ in range(R)]
        if R < 2 and C < 2:
            if dungeon[0][0] > 0:
                return 1
            else:
                return 1 - dungeon[0][0]
        
        dp[0][0] = ((0 - dungeon[0][0]) + 1, 1) if dungeon[0][0] < 0 else (1, 1)
        
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    x, y = (0, -1)
                elif j == 0:
                    x, y = (-1, 0)
                else:
                    if dp[i - 1][j][0] < dp[i][j - 1][0]:
                        x, y = (-1, 0)
                    elif dp[i - 1][j][0] > dp[i][j - 1][0]:
                        x, y = (0, -1)
                    else:
                        if dp[i - 1][j][1] > dp[i][j - 1][1]:
                            x, y = (-1, 0)
                        else:
                            x, y = (0, -1)
                            
                o_ile_zwiekszyc_start = (dp[i + x ][j + y][1] + dungeon[i][j])
                if o_ile_zwiekszyc_start <= 0:
                    o_ile_zwiekszyc_start = 1 - o_ile_zwiekszyc_start
                else: 
                    o_ile_zwiekszyc_start = 0
                curr_min_sum = 1 if (dp[i + x ][j + y][1] + dungeon[i][j]) < 0 else dp[i + x ][j + y][1] + dungeon[i][j]
                    
                curr_min_start = dp[i + x ][j + y][0] + o_ile_zwiekszyc_start 
                dp[i][j] = (curr_min_start, curr_min_sum)
        print(dp)
        
        return dp[-1][-1][0]
    
    
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        inf = 10**12
        n, m = len(dungeon), len(dungeon[0])
        dp = [inf] * (m + 1)
        dp[m-1] = 1                     # wirtualna komórka za celem

        for r in reversed(range(n)):
            for c in reversed(range(m)):
                need = min(dp[c], dp[c+1]) - dungeon[r][c]
                dp[c] = max(1, need)
        return dp[0]
