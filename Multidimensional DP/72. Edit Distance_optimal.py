class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # upewnij się, że word2 jest krótszy => mniej pamięci
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)

        prev = list(range(n+1))  # row for i-1
        curr = [0]*(n+1)

        for i in range(1, m+1):
            curr[0] = i          # dp[i][0]
            for j in range(1, n+1):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                curr[j] = min(
                    prev[j] + 1,      # delete
                    curr[j-1] + 1,    # insert
                    prev[j-1] + cost  # replace / copy
                )
            prev, curr = curr, prev   # zamiana ról
        return prev[n]