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