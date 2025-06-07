from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # pass1 = True
        # while pass1:
        #     if nums[0] < 0:
        #         nums = nums[1:]
        #     elif nums[-1] < 0:
        #         nums = nums[:-1]
        #     else:
        #         pass1 = False
        # pass2 = True
        mx = []
        # i = 0
        # while pass2
        l = len(nums)
        # for i in range(len(nums)):
        #     if sum(nums[:i]) > sum(mx):
        #         mx = nums[:i]
        # for i in range(len(nums)):
        #     if sum(nums[i:]) > sum(mx):
        #         mx = nums[i:]

        for i in range(l):
            for j in range(l):
                # start = j
                # end = j + i 
                if j + i < l:
                    end = j + i + 1
                # elif i == 0
                else:
                    end = -1
                tmp = nums[j:end]
                # print(tmp, j, end)
                if sum(tmp) > sum(mx) or not mx:
                    mx = tmp

        return sum(mx)
    
    
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Edge-case: if nums is empty, conventionally return 0
        if not nums:
            return 0
        
        # Initialize both to nums[0]
        current_sum = best_sum = nums[0]
        
        # Iterate from the second element onward
        for x in nums[1:]:
            # Either extend the previous subarray, or start a new one at x
            current_sum = max(x, current_sum + x)
            # Update the global best if needed
            best_sum = max(best_sum, current_sum)
        
        return best_sum
    

def max_sub_array(list_s):
    if not list_s:
        return 0
    
    current_sum = best_sum = list_s[0]
    
    for x in list_s[1:]:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    
    return best_sum





def max_sub_array(l):
    if not l:
        return 0
    
    current_sum = best_sum = l[0]
    
    for x in l[1:]:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
        
    return best_sum




def max_sub_array(l):
    
    if not l:
        return 0
    
    current_sum = best_sum = l[0]
    
    for i in l[1:]:
        current_sum = max(i, current_sum + i)
        best_sum = max(best_sum, current_sum)
        
    return best_sum