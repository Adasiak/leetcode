def tree_sum(nums):
    nums.sort()
    n = len(nums)
    res: list[list[int]]
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        target = -nums[i]
        
        left, right = i +1, n-1
        while left < right:
            s = nums[left] + nums[right]
            
            if s == target:
                res.append([nums[i], nums[left], nums[right]])
                
                left_val = nums[left]
                
                while left < right and nums[left] == left_val:
                    left +=1
                
                right_val = nums[right]
                
                while left < right and nums[right] == right_val:
                    right -=1
            elif s < target:
                left += 1
            else:
                right += 1
    return res