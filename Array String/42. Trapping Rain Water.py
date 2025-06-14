from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0  
        counter = 0
        z = 0
        while len(height) > 2:
            print(z, height)
            z+=1
            skip = False
            if height[0] == 0:
                height.pop(0)
                skip = True
            if height[-1] == 0:
                height.pop()
                skip = True
            if not skip:
                counter += height.count(0)
                for i in range(len(height)):
                    if height[i] != 0:
                        height[i] -= 1
            if len(height) - height.count(0) <=1:
                break
            # print(i, height)
            # i+=1
        return counter 
    
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0                    # need at least 3 bars to hold water

        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                # left side limits the water level
                if height[left] >= left_max:
                    left_max = height[left]        # new wall
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # right side limits the water level
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
    
    
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left, right = 0, len(height) -1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water