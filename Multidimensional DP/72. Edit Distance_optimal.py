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



class Solution:  
    def minDistance(self, word1: str, word2: str) -> int:
        # upewnij się, że word2 jest krótszy => mniej pamięci
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)   
        prev = list(range(n+1))  # wiersz dp[0][*]  (koszt wstawień)
        curr = [0]*(n+1)         # pusty bufor na wiersz dp[1][*] itd.

        for i in range(1, m+1):
            curr[0] = i          # dp[i][0] – koszt i usunięć
            for j in range(1, n+1):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                curr[j] = min(
                    prev[j] + 1,      # dp[i-1][j] + delete
                    curr[j-1] + 1,    # dp[i][j-1] + insert
                    prev[j-1] + cost  # dp[i-1][j-1] + replace/copy
                )
            prev, curr = curr, prev   # zamiana ról, czyszczenie curr w kolejnej iteracji
        return prev[n]
