class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem_list = []
        for i in range(len(nums)):
            if nums[i] in mem_list:
                return [mem_list.index(nums[i]), i]
            else:
                mem_list.append(target - nums[i])
                


# słownik przyspiesza                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #brute force solution: check from left with future nums
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        #idx solution: check from left with the previous nums
        pre_idx = {}
        for i,num in enumerate(nums):
            if target - num in pre_idx:
                return [i,pre_idx[target - num]]
            pre_idx[num] = i