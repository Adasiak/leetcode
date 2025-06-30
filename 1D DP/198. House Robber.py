from typing import List

#  ma problemy 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        best_sum = 0
        for i in range(2, len(nums)):
            for j in range(i):
                best_sum = max(best_sum, sum(nums[j::i]))
        return best_sum
    

# to dziala i jest lepsze 

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        sums[1] = nums[1]
        for i in range(2, len(sums)):
            tmp = max(sums[:i - 1])
            if tmp > 0:
                sums[i] = nums[i] + tmp
            else:
                sums[i] = nums[i]
        return max(sums)
        