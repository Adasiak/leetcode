from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return min(nums)