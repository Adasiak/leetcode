from typing import List
import heapq

class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     res = []
        
    #     for i in nums1:
    #         for j in nums2:
    #             heapq.heappush(res, (i + j, i, j))
    #     return heapq.nsmallest(k, res)
    
    
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        for a in nums1:
            for b in nums2:
                heapq.heappush(heap, (a+b, a, b))   # ① pierwszy element = suma
        ans = []
        while heap and len(ans) < k:                # ② pobierasz k najmniejszych
            _, a, b = heapq.heappop(heap)
            ans.append([a, b])
        return ans



import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        # (suma, idx1, idx2)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)

        ans = []
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):                     # w tym samym wierszu jest kolejna para
                nxt = (nums1[i] + nums2[j+1], i, j+1)
                heapq.heappush(heap, nxt)

        return ans




class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        
        ans = []
        
        while heap and len(ans) < k:
            _, i, j  = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                nxt = (nums1[i] + nums2[j + 1], i, j + 1)
                heapq.heappush(heap, nxt)
        return ans