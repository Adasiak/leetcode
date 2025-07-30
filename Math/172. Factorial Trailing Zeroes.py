class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math

        z = math.factorial(n)
        if z == 0:
            return 1
        elif 0 < z < 10:
            return 0
        cnt = 0
        while z % 10 == 0:
            cnt += 1
            z //= 10
        return cnt