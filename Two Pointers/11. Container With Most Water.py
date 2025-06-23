from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max_capacity = 0
        left = left_tmp = 0
        hei = 0
        right = len(height) - 1
        # for right in reversed(range(1, len(height))):
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            # print(height[left], left , height[right])
            # if right > left:
            hei = min(height[right], height[left])
            tmp_capacity = hei * (right-left)
            #     print(tmp_capacity)
            if tmp_capacity > max_capacity:
                max_capacity = tmp_capacity
            #     tmptmp = 0
            #     # while height[right] > height[left] and right - left > 1:
            #     while right - left_tmp > 1:
            #         left_tmp += 1
            #         if right > left_tmp:
            #             hei_tmp = min(height[right], height[left_tmp])
            #             tmptmp = hei_tmp * (right-left_tmp)
            #             if tmptmp > max_capacity:
            #                 left = left_tmp
            #                 break
        
        
        
        return max_capacity
    
    
    
    
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max_capacity = 0
        left = 0
        hei = 0
        right = len(height) - 1
        while left < right:
            hei = min(height[right], height[left])
            tmp_capacity = hei * (right-left)
            if tmp_capacity > max_capacity:
                max_capacity = tmp_capacity
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_capacity