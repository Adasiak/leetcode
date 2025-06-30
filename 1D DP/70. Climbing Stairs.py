class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            c = a
            a = b
            b = a + c
        
        return b