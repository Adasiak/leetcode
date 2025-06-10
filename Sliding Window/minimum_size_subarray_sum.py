# from typing import List
# # dziala jesli kolejnosc nie ma znaczenia 

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if not nums or sum(nums) < target:
#             return 0
#         nums.sort()
#         nums.reverse()
#         tmp = []
        
#         print(nums)
#         for i, v in enumerate(nums):
#             tmp.append(v)
#             if sum(tmp) >= target: 
#                 return len(tmp)
#             print(i, target - sum(tmp))
#         return 0
    



# from typing import List


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if not nums or sum(nums) < target:
#             return 0
#         l = len(nums)
#         for i in range(l):
#             for j in range(l):
#                 if j + i < l:
#                     end = j + i + 1
#                 else:
#                     break
#                 tmp = nums[j:end]
#                 print(tmp, j, i, end)
#                 if sum(tmp) >= target:
#                     return len(tmp)
#         return 0
    



# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if not nums or sum(nums) < target:
#             return 0
        
#         current_sum = -1
#         min_l = float("inf")
#         i = 0
#         l = len(nums)
#         for i in range(l):
#             tmp, current_sum = [nums[i]], nums[i] 
#             if current_sum >= target:
#                 print(tmp)
#                 return 1
#             for j in nums[i+1:]:
#                 current_sum += j
#                 tmp.append(j)
#                 if current_sum >= target:
#                     min_l = min(len(tmp), min_l)
#                     print(tmp)
#                     break      
#         return 0
            
            
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if not nums or sum(nums) < target:
#             return 0
        
#         current_sum = -1
#         min_l = float("inf")
#         i = 0
#         l = len(nums)
#         for i in range(l):
#             tmp, current_sum = [nums[i]], nums[i] 
#             if current_sum >= target:
#                 print(tmp)
#                 return 1
#             for j in nums[i+1:]:
#                 current_sum += j
#                 tmp.append(j)
#                 if current_sum >= target:
#                     print(type(len(tmp)))
#                     min_l = min(len(tmp), min_l)
#                     print(tmp)
#                     break      
#         return 0
            
            
            
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or sum(nums) < target:
            return 0
        len_nums = len(nums)
        min_l = float("inf")
        current_sum, currnet_len, i, j = 0, 0, 0, 0
        while i < len_nums:
            current_sum +=  nums[j]
            currnet_len += 1
            if current_sum >= target:
                i, j = i + 1, i
                min_l = min(min_l, currnet_len)
                current_sum, currnet_len = 0, 0
            elif j + 1 == len_nums:
                i, j = i + 1, i
            else:
                j += 1
        return min_l
    

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        best = float('inf')           # minimalna długość znalezionego okna

        for right, val in enumerate(nums):
            curr_sum += val           # powiększamy prawe ramię okna

            # gdy suma spełnia warunek, próbujemy okno skrócić od lewej
            while curr_sum >= target:
                best = min(best, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if best == float('inf') else best
    
    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_l = float("inf")
        
        for right, val in enumerate(nums):
            current_sum += val
            
            while current_sum >= target:
                min_l = min(min_l, right - left +1)
                current_sum -= nums[left]
                left += 1
        return 0 if min_l == float("inf") else min_l
    
    


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_l = float("inf")
        
        for right, val in enumerate(nums):
            curr_sum += val
            
            while curr_sum >= target:
                min_l = (min_l, right - left +1)
                curr_sum -= nums[left]
                left += 1
        return 0 if min_l == float("inf") else min_l
    
    
    
    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            left = 0
            curr_sum = 0
            min_len = float("inf")
            len_nums = len(nums)
            
            for right in range(len_nums):
                curr_sum += len_nums[right]
                
                while curr_sum >= target:
                    min_len = min(min_len, right - left + 1)
                    curr_sum -= left
                    left += 1
            return 0 if min_len == float("inf") else min_len
        
        
        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0 
        min_len = float("inf")
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= left
                left += 1
                
        return 0 if min_len == float("inf") else min_len