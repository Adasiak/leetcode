from typing import List
from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        # cur = 0
        maxx = deque()
        for num in set_nums:
            curr = num
            tmp = 1
            if num - 1 not in set_nums:
                while curr + 1 in set_nums:
                    tmp += 1
                    curr += 1
                if not maxx:
                    maxx.append(tmp)
                else:
                    tmp2 = maxx.pop()
                    if tmp2 > tmp:
                        maxx.append(tmp2)
                    else:
                        maxx.append(tmp)    
        max_len = maxx.pop()
        return max_len 
        