class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(10):
            if n == 1:
                return True
            digits = list(str(n))
            ss = 0
            for digit in digits:
                ss += (int(digit))**2
            n = ss
        return False

