from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_of_list = len(nums)
        if k == 0 or len_of_list < 2 :
            return
        
        k = k % len_of_list
        nums[:] = nums[-k:] + nums[:-k]
        return
        

# nums = [1,2,3,4]
# k = 2
# print(Solution.rotate(nums, k))



from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list_len = len(nums)
        if list_len == 0:
            return
        
        k = k % list_len
        nums[:] = nums[-k:] + nums[:-k]
        return



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return 0
        
        l = k % len(nums)
        nums = nums[-l:] + nums[:-l]
        return nums
    
    