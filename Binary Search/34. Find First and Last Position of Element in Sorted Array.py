from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:                        # edge‑case
            return [-1, -1]

        def extreme(is_left: bool) -> int:
            lo, hi = 0, len(nums) - 1
            best = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    best = mid              # candidate answer
                    # keep looking to expand in chosen direction
                    if is_left:
                        hi = mid - 1        # go further left
                    else:
                        lo = mid + 1        # go further right
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return best

        left  = extreme(True)
        right = extreme(False)
        return [left, right]