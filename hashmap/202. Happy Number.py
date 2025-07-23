class Solution:
    def isHappy(self, n: int) -> bool:
        def dfs(m):
            if m < 10:
                return False
            digits = list(str(m))
            ss = 0
            for digit in digits:
                ss += (int(digit))**2
            if ss == 1:
                return True
            else:
                dfs(ss)
            print(digits)
        dfs(n)
        return False
    
    
    
    
7
49
16 + 81 = 97
81 + 49 = 130
1 + 9 = 10
1 + 0 = 1
