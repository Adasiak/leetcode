from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0
        
        if not coins:
            return -1
        
        INF = 10**12
        dp = [INF] * (amount + 1)
        dp[0] = 0    
    
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == INF else dp[amount]
    
    
    
from typing import List

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
            for i in range(coin, amount + 1):   # zaczynamy od jej wartości
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == INF else dp[amount]
