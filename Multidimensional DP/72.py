class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n =  len(word1), len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        
        prev = [i for i in range(n + 1)]
        curr = [n] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                
                curr[j] = min(
                    prev[j] + 1,
                    curr[j - 1] + 1,
                    prev[j - 1] + cost,
                )
            prev, curr = curr, prev
        return prev[-1]
        
          
        
        
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



