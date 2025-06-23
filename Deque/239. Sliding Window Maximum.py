from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_elem_prev_win = 0
        # last_elem_new_window = 0
        last_max = 0
        cur_max = 0
        all_sums = []
        for i in range(k-1, len(nums)):
            tmp = nums[(i-k+1):(i+1)]
            # if not all_sums:
            #     tmp = nums[(i-k+1):(i+1)]
            #     cur_sum = sum(tmp)
            #     last_sum = cur_sum
            #     # first_elem_prev_win = nums[i-k+1]
            # else:
            #     cur_sum = max(last_sum - first_elem_prev_win + nums[i], last_sum)
            #     # first_elem_prev_win
            
            # print(first_elem_prev_win, last_sum, cur_sum, tmp)
            # first_elem_prev_win = nums[i-k+1]
            
            # print(first_elem_prev_win, last_sum, cur_sum)
            
            all_sums.append(max(tmp))
            # print(all_sums)
        return all_sums
    
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_elem_prev_win = 0
        last_max = 0
        all_maxs = []
        for i in range(k-1, len(nums)):
            print(nums[i])
            # tmp = nums[(i-k+1):(i+1)]
            if not all_maxs:
                tmp = nums[(i-k+1):(i+1)]
                first_elem_prev_win = nums[(i-k+1)]
                last_max = max(tmp)
                # curr_max = last_max
            else:
                if first_elem_prev_win == last_max:
                    tmp = nums[(i-k+1):(i+1)]
                    last_max = max(tmp)
                elif nums[i] > last_max:
                    last_max = nums[i]
            first_elem_prev_win = nums[(i-k+1)]
            all_maxs.append(last_max)
            # print(all_sums)
        return all_maxs
    
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
                for elem in nums[(i-k+1):(i+1)]:
                    que = elem
                # first_elem_prev_win = que[0]
                last_max = max(que)
                # curr_max = last_max
            else:
                first_elem_prev_win = que.popleft()
                que.append(nums[i])
                if first_elem_prev_win == last_max:
                    tmp = nums[(i-k+1):(i+1)]
                    last_max = max(tmp)
                elif que[-1] > last_max:
                    last_max = que[-1]
            all_maxs.append(last_max)
            # print(all_sums)
        return all_maxs


from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq: deque[int] = deque()   # przechowuje INDeksy w malejącym porządku wartości
        out: List[int] = []

        for i, val in enumerate(nums):
            # 1) usuń z prawej wszystkie elementy ≤ bieżącej wartości
            while dq and nums[dq[-1]] <= val:
                dq.pop()

            # 2) dołóż bieżący indeks
            dq.append(i)

            # 3) usuń z lewej indeks, który wypadł poza okno
            if dq[0] == i - k:
                dq.popleft()

            # 4) gdy okno gotowe, zapisz maksimum
            if i >= k - 1:
                out.append(nums[dq[0]])

        return out


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        out = []
        
        for i, val in enumerate(nums):
            while dq and nums[dq[-1]] <= val:
                dq.pop()
            
            dq.append(i)
            
            if dq[0] == i - k:
                dq.popleft()
            
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out
    
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        for i, v in enumerate(nums):
            while q and nums[q[-1]] <= v:
                q.pop()
            
            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
            
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res
    
    
    


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        for i, v in enumerate(nums):
            while q and nums[q[-1]] <= v:
                q.pop()
            
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            
            if q[0] >= k - 1:
                res.append(nums[q[0]])
        return res