from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        
        INF = 10**12
        tabel = [INF] * (amount + 1)
        tabel[0] = 0
        for coin in coins:
            for i in range(coin, len(tabel)):
                tabel[i] = min(tabel[i], tabel[i - coin] + 1)
        return tabel[-1] if tabel[-1] != INF else -1
    


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10**9
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != INF else -1