from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            s = s.replace(word,"")
        return True if not s else False
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        point = 0
        settt = set(wordDict)
        ss = s
        for i in range(1, len(s) + 1):
            tmp = s[point:i]
            
            if tmp in settt:
                point = i
                ss = ss.replace(tmp, "", 1)
                # wordDict.remove(tmp)
                print(tmp, ss, settt)
        return True if not ss else False
    


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[0] = True
        sett = set(wordDict)
        
        # i = 0
        for j in range(1, len(dp)):
            for i in range(j):
                # tmp_with_pointer = True if s[i:j] in sett else False
                # if tmp_with_pointer:
                #     i = j
                # tmp = True if s[:j] in sett else False
                
                # dp[i] = max(tmp, tmp_with_pointer)
                if dp[i] == True and s[i:j] in sett:
                    dp[j] = True
                    break
        return dp[-1]
        
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[0] = True
        sett = set(wordDict)
        
        for j in range(1, len(dp)):
            for i in range(j):
                if dp[i] == True and s[i:j] in sett:
                    dp[j] = True
                    break
        return dp[-1]
    
    
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        sett = set(wordDict)
        for j in range(1, len(dp)):
            for i in range(j):
                if dp[i] == True and s[i:j] in sett:
                    dp[j] = True
                    break
        return dp[-1]