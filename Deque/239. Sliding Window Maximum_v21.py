from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_elem_prev_win = 0
        last_max = 0
        que = deque()
        all_maxs = []
        for i in range(k-1, len(nums)):
            print(nums[i])
            if not all_maxs:
                que = nums[(i-k+1):(i+1)]
                # first_elem_prev_win = que[0]
                last_max = max(que)
                # curr_max = last_max
            else:
                first_elem_prev_win = que.popleft
                que.append(nums[i])
                if first_elem_prev_win == last_max:
                    tmp = nums[(i-k+1):(i+1)]
                    last_max = max(tmp)
                elif que[-1] > last_max:
                    last_max = nums[i]
            all_maxs.append(last_max)
            # print(all_sums)
        return all_maxs