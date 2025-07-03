from heapq import heappop, heappush
from typing import List

# dp 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        
        prev = [i for i in range(n + 1)]
        curr = [0] * (n + 1)            
        
        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i -1] == word2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                
                curr[j] = min(
                    prev[j - 1] + cost,
                    curr[j - 1] + 1,
                    prev[j] + 1,
                )
            prev, curr = curr, prev
        return prev[-1]



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, w = len(s1), len(s2), len(s3)
        if m + n != w:
            return False
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(1, n + 1):
            # wiersz zerowy: używamy tylko s2
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        
        for i in range(1, m + 1):
            # kolumna 0: używamy tylko s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, n + 1):
                takes1 = dp[j] and s1[i - 1] == s3[i + j - 1] # dp[j] to stara wartość (wiersz powyżej)
                takes2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1] # dp[j-1] to bieżąca wartość w wierszu
                take = takes1 or takes2
                dp[j] =  take
        
        return dp[-1]
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev, curr = curr, prev
        return prev[-1]
                
                

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        INF = 10**12
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:                      # każda moneta
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == INF else dp[amount]
    
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        sums[1] = nums[1]
        for i in range(2, len(sums)):
            tmp = max(sums[:i - 1])
            if tmp > 0:
                sums[i] = nums[i] + tmp
            else:
                sums[i] = nums[i]
        return max(sums)

#  djikstry
   
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
        
        
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        g = [[] for _ in range(n)]
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        
        INF = 10 ** 20
        
        dist = [INF] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, v = heappop(pq)
            
            if d > dist[v]:
                continue
            
            for next, w in g[v]:
                nd = d + w
                if nd < dist[next]:
                    dist[next], ways[next] = nd, ways[v]
                    heappush(pq, (nd, next))
                elif nd ==  dist[next]:
                    ways[next] = (ways[next] + ways[v]) % MOD
        return ways[n - 1] % MOD