from typing import List
from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return 0
        kaczka = Counter(nums)
        top = heapq.nlargest(k, kaczka, key=kaczka.get)
        return top
        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return 0
        d = Counter(nums)
        top = heapq.nlargest(k, d, key=d.get)
        return top