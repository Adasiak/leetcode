from typing import List

import math

# nums = [2, 3, 4]
# wynik = math.prod(nums)
import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n            # 1. prefix products

        # Left → right: store product of elements to the left of i
        for i in range(1, n):
            out[i] = out[i - 1] * nums[i - 1]

        # Right ← left: running suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out